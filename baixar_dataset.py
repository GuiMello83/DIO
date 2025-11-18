import os
from icrawler.builtin import BingImageCrawler
import logging

logging.basicConfig(level=logging.INFO)

def download_images(name, num_images=200):
    """Downloads images using BingImageCrawler."""
    
    image_dir = os.path.join(os.getcwd(), f"dataset_{name.replace(' ', '_').lower()}")
    
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
        print(f"Diretório '{image_dir}' criado.")
    
    # Usa BingImageCrawler em vez de GoogleImageCrawler
    crawler = BingImageCrawler(
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': image_dir}
    )
    
    search_filters = dict(
        size='medium',
        type='photo'
    )
    
    print(f"Iniciando download de {num_images} imagens para {name}...")
    
    crawler.crawl(
        keyword=f"{name} actor face", 
        filters=search_filters, 
        max_num=num_images
    )
    print(f"Download de {name} concluído.")

# Execução Principal
download_images("Tom Cruise")
download_images("Brad Pitt")
