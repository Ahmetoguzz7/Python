class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"'{task}' görevi eklendi.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"'{task}' görevi tamamlandı.")
        else:
            print(f"'{task}' görevi bulunamadı.")

    def show_tasks(self):
        if self.tasks:
            print("Yapılacaklar Listesi:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Yapılacak bir görev bulunmamaktadır.")

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Görev ekle")
        print("2. Görev tamamla")
        print("3. Görevleri göster")
        print("4. Çıkış")
        choice = input("Seçiminizi yapın (1/2/3/4): ")

        if choice == '1':
            task = input("Yapılacak görevi girin: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Tamamlanan görevi girin: ")
            todo_list.complete_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
