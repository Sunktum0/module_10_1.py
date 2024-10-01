import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Задержка 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

start_time = time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = time()
print(f"Время выполнения обычных вызовов: {end_time - start_time:.2f} сек")

# Функция для запуска записи в новом потоке
def thread_function(word_count, file_name):
    write_words(word_count, file_name)

# Создание и запуск потоков
threads = []
start_time_threads = time()

for count, name in [(10, "example5.txt"), (30, "example6.txt"),
                    (200, "example7.txt"), (100, "example8.txt")]:
    thread = threading.Thread(target=thread_function, args=(count, name))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time()
print(f"Время выполнения потоков: {end_time_threads - start_time_threads:.2f} сек")