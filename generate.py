from ascii_gm.text_generator import generate_text
from ascii_gm.oracle_data import gen_data
from ascii_gm.ascii_png import create_card
from tqdm import tqdm


for idx in tqdm(range(100)):
    idx_str = str(idx).zfill(3)
    create_card(generate_text("card", gen_data), f"cards/card_{idx_str}.png")
