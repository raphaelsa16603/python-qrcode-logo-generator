
import argparse
import sys
from pathlib import Path
from typing import Optional

import qrcode
import qrcode.image.svg
from PIL import Image, ImageDraw, ImageColor
from loguru import logger


class QRCodeGenerator:
    def __init__(
        self,
        url: str,
        output_format: str = "jpg",
        output_dir: str = "output",
        size: int = 600,
        square_ratio: float = 0.25,
        square_color: str = "white",
    ) -> None:
        self.url = url
        self.output_format = output_format.lower()
        self.output_dir = Path(output_dir)
        self.size = int(size)
        self.square_ratio = float(square_ratio)
        self.square_color = square_color
        self.output_path = self.output_dir / f"qrcode_logo.{self.output_format}"

    def _validate_color(self, color: str) -> None:
        try:
            ImageColor.getrgb(color)
        except Exception as exc:
            raise ValueError(f"Cor inválida: '{color}'. Use nomes CSS (ex.: white, black, red) ou HEX (#RRGGBB).") from exc

    def generate_qr(self) -> Optional[Image.Image]:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        if self.output_format == "svg":
            factory = qrcode.image.svg.SvgImage
            img_svg = qr.make_image(image_factory=factory)
            svg_data = img_svg.to_string().decode("utf-8")

            if self.square_ratio > 0:
                import xml.etree.ElementTree as ET
                root = ET.fromstring(svg_data)
                viewBox = root.attrib.get("viewBox", "0 0 290 290")
                _, _, width, height = map(float, viewBox.split())
                square_size = min(width, height) * self.square_ratio
                left = (width - square_size) / 2.0
                top = (height - square_size) / 2.0
                rect = ET.Element("rect", {
                    "x": str(left),
                    "y": str(top),
                    "width": str(square_size),
                    "height": str(square_size),
                    "fill": self.square_color,
                })
                root.append(rect)
                svg_data = ET.tostring(root, encoding="unicode")

            self.save_svg(svg_data)
            return None

        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        img = img.resize((self.size, self.size))
        return img

    def add_center_square(self, img: Image.Image) -> Image.Image:
        if self.output_format == "svg":
            return img
        self._validate_color(self.square_color)
        draw = ImageDraw.Draw(img)
        width, height = img.size
        square_size = int(min(width, height) * self.square_ratio)
        left = (width - square_size) // 2
        top = (height - square_size) // 2
        right = left + square_size
        bottom = top + square_size
        draw.rectangle([left, top, right, bottom], fill=self.square_color)
        return img

    def save_raster(self, img: Image.Image) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        img.save(self.output_path)

    def save_svg(self, svg_text: str) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(svg_text, encoding="utf-8")

    def run(self) -> None:
        img = self.generate_qr()
        if img is not None:
            if self.square_ratio > 0:
                img = self.add_center_square(img)
            self.save_raster(img)


def _parse_args(argv):
    import argparse
    from PIL import ImageColor

    parser = argparse.ArgumentParser(
        prog="gerador_qr_code.py",
        description="Gerador de QR Code com quadrado central para logo (JPG/BMP/SVG).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--url", help="URL a codificar no QR Code")
    parser.add_argument("--filetype", choices=["jpg", "bmp", "png", "svg"], default="jpg", help="Formato de saída")
    parser.add_argument("--size", type=int, default=600, help="Tamanho (pixels) para raster")
    parser.add_argument("--squareratio", type=float, default=25.0, help="Tamanho do quadrado central (%% do lado)")
    parser.add_argument("--squarecolor", default="white", help="Cor do quadrado (nome CSS ou HEX)")
    parser.add_argument("--outputdir", default="output", help="Diretório de saída")
    parser.add_argument("legacy_url", nargs="?", help=argparse.SUPPRESS)
    parser.add_argument("legacy_format", nargs="?", help=argparse.SUPPRESS)

    args = parser.parse_args(argv)

    if not args.url and args.legacy_url:
        args.url = args.legacy_url
    if args.legacy_format and args.filetype == parser.get_default("filetype"):
        args.filetype = args.legacy_format.lower()

    if not args.url:
        parser.error("A URL é obrigatória. Use --url=<...> ou modo legado: python gerador_qr_code.py <URL> <FORMATO>")

    if not (50 <= args.size <= 5000):
        parser.error("--size deve estar entre 50 e 5000.")

    if not (0.0 <= args.squareratio <= 90.0):
        parser.error("--squareratio deve estar entre 0 e 90.")
    args.squareratio = args.squareratio / 100.0

    try:
        ImageColor.getrgb(args.squarecolor)
    except Exception:
        parser.error("--squarecolor inválido. Use nome CSS ou HEX (#RRGGBB).")

    return args


def main(argv=None) -> int:
    args = _parse_args(argv or sys.argv[1:])
    logger.info(f"Gerando QR: {args.url}  formato={args.filetype} size={args.size} ratio%={args.squareratio*100} color={args.squarecolor}")

    gen = QRCodeGenerator(
        url=args.url,
        output_format=args.filetype,
        output_dir=args.outputdir,
        size=args.size,
        square_ratio=args.squareratio,
        square_color=args.squarecolor,
    )
    gen.run()
    print(f"Saida: {gen.output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
