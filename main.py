import os
import CRUD

if __name__ == "__main__":
    sysetem_operasi = os.name
    match sysetem_operasi:
            case "poxis": os.system("clear")
            case "nt": os.system("cls")
        
    print("="*60)
    print("+"*20,"Program Data siswa","+"*20)
    print("="*60)

    # cheking database
    CRUD.init_console()


    while(True):
        match sysetem_operasi:
            case "poxis": os.system("clear")
            case "nt": os.system("cls")

        print("="*60)
        print("+"*20,"Program Data siswa","+"*20)
        print("="*60)

        print("\nMENU\n")
        print("1. Tampilkan data")
        print("2. Buat data")
        print("3. Update data")
        print("4. Delete data\n")

        user_options = input("masukkan pilihan: ")
        print("\n---------------------------------------------------------------------\n")
        match user_options:
            case "1":
                CRUD.read_database()
            case "2":
                CRUD.create_data()
            case "3":
                CRUD.update_database()
            case "4":
                CRUD.delete_database()

        print("\n---------------------------------------------------------------------\n")
        # print("-"*60,"\n")

        check = input("apakah anda ingin lanjut (y/n): ").lower()
        if check == "n":
            break
    

        