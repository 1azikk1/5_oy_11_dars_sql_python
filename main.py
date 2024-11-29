from database import db


if __name__ == "__main__":
    while True:
        command = input("Buyruqni kiriting: ").lower()
        if command == 'stop':
            print("Dastur to'xtadi!")
            break
        elif command == 'help':
            print("Buyruqlar:\nStop - dasturni to'xtatish.\n"
                  "1.Create Categories - categories jadvalini yaratish.\n"
                  "2.Create News - news jadvalini yaratish.\n"
                  "3.Create Comments - comments jadvalini yaratish.\n"
                  "4.Add Column Views - news jadvaliga yangi ustun qo'shish.\n"
                  "5.Change Type comments - comments jadvalidagi author_name ustuni ma'lumot turini o'zgartirish.\n"
                  "6.Insert Categories - categories jadvaliga ma'lumot qo'shish.\n"
                  "7.Insert News - news jadvaliga ma'lumotlar qo'shish.\n"
                  "8.Insert Comments - comments jadvaliga ma'lumotlar qo'shish.\n"
                  "9.Increase Views - news jadvalidagi ko'rishlar sonini yangilash.\n"
                  "10.Select Alias - alias ustunidan foydalanib ma'lumotlarni chiqarish.\n"
                  "11.Select Technology - technology kategoriyasidagi yangiliklarni chiqarish.\n"
                  "12.Update Is_Published - is_published ustunini yangilash.\n"
                  "13.Delete Old Comments - yaratilganiga 1 yil bo'lgan izohlarni o'chirib tashlash.\n"
                  "14.Sorted News - tartiblangan yangiliklani chiqarish.\n"
                  "15.Select Filtered Views - 10 va 100 orasidagi ko'rishlar soniga ega xabarlarni chiqarish.\n"
                  "16.Select A - A harfi bilan boshlangan author_name ni chiqaradi.\n"
                  "17.Select Null - author_name null bo'lgan comment larni olib berish.\n"
                  "18.Select Categories - categoriyalarda nechtadan yangiliklar borligini ko'rish.\n"
                  "19.Add Constraint - news jadvalidagi title ustuniga unique cheklovini o'rnatish.")
        elif command == 'create categories':
            db.create_table_categories()
            print("Jadval yaratildi!")
        elif command == 'create news':
            db.create_table_news()
            print("Jadval yaratildi!")
        elif command == 'create comments':
            db.create_table_comments()
            print("Jadval yaratildi!")
        elif command == 'add column views':
            try:
                db.alter_table_news()
                print("Yangi ustun qo'shildi!")
            except Exception as e:
                print(f"Ustun qo'shish uchun jadval mavjud emas!\n{e}")

        elif command == 'change type comments':
            try:
                db.alter_table_comments()
                print("Author_name ustuni ma'lumot turi text ga o'zgartirildi!")
            except Exception as e:
                print(f"Yangilash uchun ma'lumot mavjud emas!\n{e}")

        elif command == 'insert categories':
            try:
                db.insert_categories("Technology", "So'nggi texnoligiyaga oid yangiliklar!")
                db.insert_categories("Sports", "Sport xabarlari haqida yangiliklar!")
                db.insert_categories("Health", "Insonning hayoti va sog'lom turmush tarzi haqida!")
                print("Barcha ma'lumotlar saqlandi!")
            except Exception as e:
                print(f"Categories jadvali yaratilmagan!: {e}")

        elif command == 'insert news':
            try:
                db.insert_news(1, "SamsungGalaxy S25 ULTRA Taqdimoti", "Mobil qurilmaning taqdimoti 2025-yilda boladi!")
                db.insert_news(2, "Boksdagi muvaffaqiyat", "Hasanboy Do'stmatov Olimpiadadagi 2 - oltiniga erishdi!")
                db.insert_news(3, "Bel og'rig'ini oldini olish", "Inson serharakat bo'lishi kerak,"
                                                                 "hamda sog'lom turmush tarziga rioya qilish zarur!")
                db.insert_news(2, "O'zbekistonda Futbol", "Terma jamoamiz Qatarga 3:2 hisobida mag'lub bo'ldi.")
                db.insert_news(1, "New GPU", "NVIDIA companiiyasi yangi RTX 5090 GPU sini taqdim etishi kutilmoqda.")
                print("Barcha ma'lumolar saqlandi!")
            except Exception as e:
                print(f"News jadvali yaratilmagan!\n{e}")

        elif command == 'insert comments':
            try:
                db.insert_comments(1, 'Azizbek', "Eng zo'r mobil qurilma!!!")
                db.insert_comments(2, 'rizowking', "Sportchining keyingi hayotida ham omad tilab qolamiz!")
                db.insert_comments(3, None, "Kakraz kerak edi.Belim og'rib turgandi!")
                db.insert_comments(5, 'alikk', "Narxi qancha bo'larkan?")
                db.insert_comments(4, None, "Har doimgi ishini qiliptida😆")
                print("Barcha ma'lumotlar saqlandi!")
            except Exception as e:
                print(f"Comments jadvali yaratilmagan!\n{e}")

        elif command == 'increase views':
            try:
                db.increase_news()
                print("Ko'rishlar soni yangilandi!")
            except Exception as e:
                print(f"Yangilash uchun ma'lumot mavjud emas!\n{e}")

        elif command == 'select alias':
            try:
                for i in db.select_alias():
                    print(i)
            except Exception as e:
                print(f"Jadvallar yaratilmagan!\n{e}")

        elif command == 'select technology':
            try:
                for i in db.select_technology():
                    print(i)
            except Exception as e:
                print(f"Technolog categoriyasi yaratilmagan!\n{e}")

        elif command == 'update is_published':
            try:
                db.update_is_published()
                print("Ma'lumotlar yangilandi!")
            except Exception as e:
                print(f"Yangilash uchun ma'lumot mavjud emas!: {e}")

        elif command == 'delete old comments':
            try:
                db.delete_old_comments()
                print("Izohlar o'chirildi!")
            except Exception as e:
                print(f"O'chirish uchun comments mavjud emas!\n{e}")

        elif command == 'sorted news':
            try:
                for i in db.sorted_news():
                    print(i)
            except Exception as e:
                print(f"Jadval yaratilmagan!\n{e}")

        elif command == 'select filtered views':
            try:
                for i in db.select_views():
                    print(i)
            except Exception as e:
                print(f"Jadval yaratilmagan!\n{e}")

        elif command == 'select a':
            try:
                for i in db.select_capital_a('A%'):
                    print(i)
            except Exception as e:
                print(f"Jadval yaratilmagan!\n{e}")

        elif command == 'select null':
            try:
                for i in db.select_null():
                    print(i)
            except Exception as e:
                print(f"Jadval mavjud emas!\n{e}")

        elif command == 'select categories':
            try:
                for i in db.select_categories():
                    print(i)
            except Exception as e:
                print(f"Categories jadvali mavjud emas!\n{e}")

        elif command == 'add constraint':
            try:
                db.add_constraint()
                print("Cheklov o'rnatildi!")
            except Exception as e:
                print(f"Cheklov qo'yish uchun jadval mavjud emas!\n{e}")

        else:
            print("Mavjud bo'lmagan buyruq kiritildi!")
