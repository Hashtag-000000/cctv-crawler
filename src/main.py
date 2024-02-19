from locations.yogyakarta import atcs, atcs_kota, atcs_kp, kominfo_sleman, malioboro, bantul, cctv_jogjakota, malioboro_mam
from locations.bandung import bandung
from locations.semarang import semarang
from locations.surakarta import surakarta

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Program started")
    print("Choose CCTV to run:")
    print("1. ATCS Kota")
    print("2. Kominfo Sleman CCTV")
    print("3. Bantul CCTV")
    print("4. ATCS")
    print("5. ATCS Kulon Progo")
    print("6. ATCS Malioboro")
    print("7. Semarang")
    print("8. Bandung")
    print("9. ATCS Jogja Kota")
    print("10. ATCS Surakarta")
    print("11. Malioboro Only")
    choice = input("Enter choice: ")

    if choice == '1':
        logging.info("User chose ATCS Kota")
        cctv = atcs_kota.ATCSKota()
    elif choice == '2':
        logging.info("User chose Kominfo Sleman CCTV")
        cctv = kominfo_sleman.KominfoSlemanCCTV()
    elif choice == '3':
        logging.info("User chose Bantul CCTV")
        cctv = bantul.BantulCCTV()
    elif choice == '4':
        logging.info("User chose ATCS")
        cctv = atcs.ATCS()
    elif choice == '5':
        logging.info("User chose ATCS Kulon Progo")
        cctv = atcs_kp.ATCSKulonProgo()
    elif choice == '6':
        logging.info("User chose ATCS Malioboro")
        cctv = malioboro.MaliboroCCTV()
    elif choice == '7':
        logging.info("User chose Semarang")
        cctv = semarang.Semarang()
    elif choice == '8':
        logging.info("User chose Bandung")
        cctv = bandung.Bandung()
    elif choice == '9':
        logging.info("User chose ATCS Jogja Kota")
        cctv = cctv_jogjakota.CCTVJogjaKota()
    elif choice == '10':
        logging.info("User chose ATCS Surakarta")
        cctv = surakarta.Surakarta()
    elif choice == '11':
        logging.info("User chose Malioboro Only")
        cctv = malioboro_mam.Malioboro()
    else:
        logging.error("Invalid choice")
        print("Invalid choice!")
        return
    
    try:
        cctv.run()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
