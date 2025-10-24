import sys
import qrcode
from PIL import Image, ImageDraw
from loguru import logger
from pathlib import Path


class QRCodeGenerator:
    def __init__(self, url: str, output_format: str = "jpg", output_dir: str = "output", size: int = 600):
        """
        Classe para gerar QR Codes com espaço central para logo.
        """
        self.url = url
        self.output_format = output_format.lower()
        self.output_dir = Path(output_dir)
        self.size = size

        self.output_path = self.output_dir / f"qrcode_logo.{self.output_format}"

    def generate_qr(self):
        """
        Gera o QR Code com configuração de alta correção de erro.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        if self.output_format == "svg":
            img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
            return img

        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        img = img.resize((self.size, self.size))
        return img

    def add_center_square(self, img, square_ratio: float = 0.25, color: str = "white"):
        """
        Adiciona um quadrado central no QR Code.
        """
        if self.output_format == "svg":
            logger.warning("Quadrado central não é aplicável a SVG puro.")
            return img

        draw = ImageDraw.Draw(img)
        width, height = img.size
        square_size = int(min(width, height) * square_ratio)
        left = (width - square_size) // 2
        top = (height - square_size) // 2
        right = left + square_size
        bottom = top + square_size
        draw.rectangle([left, top, right, bottom], fill=color)
        return img

    def save(self, img):
        """
        Salva o QRCode no formato solicitado.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        img.save(self.output_path)
        logger.success(f"QR Code salvo com sucesso em: {self.output_path.resolve()}")

    def run(self):
        """
        Executa o pipeline completo.
        """
        img = self.generate_qr()
        if self.output_format != "svg":
            img = self.add_center_square(img)
        self.save(img)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python gerador_qr_code.py <URL> <FORMATO>")
        print("Exemplo: python gerador_qr_code.py http://exemplo.com svg")
        sys.exit(1)

    url = sys.argv[1]
    formato = sys.argv[2]

    logger.info(f"Gerando QRCode para: {url} no formato {formato}")
    qr = QRCodeGenerator(url, formato)
    qr.run()
