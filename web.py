import socket


def web_ttit_proj(): #Заключаем набор серверных инструкций в функцию
    server = socket.create_server(('127.0.0.1', 8080)) #Создание сервер и привязываем порт и адрес
    server.listen(1) #Прослушивает порт 8080 на предмет сигналов
    while True: # Бесконечный цикл
        print("process poshel")
        client_socket, address = server.accept() #Принимает отправленные запросы
        data = client_socket.recv(1024).decode('utf-8') #Получаем содержимое запроса(размер пакета в байтах)
        content = load_request_page(data) #Обработка запроса
        client_socket.send(content) #Ответ сервера
        client_socket.shutdown(socket.SHUT_WR) #Закрываем соединение после отправки ответа


def load_request_page(request_data): # Функция обработчика(передаем текст запроса клиента)
    HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n" #Указываем заголовок
    path = request_data.split(' ')[1] # Распарсим первую строку(запрашиваемый файл)
    response = ''
    with open('html' + path, 'rb') as file: #Открываем папку и вычитываем содержимое в байтовом виде
        response = file.read()
    return HDRS.encode('utf-8') + response #Возвращаем цельный байтовый ответ


if __name__ == '__main__': #Отсюда программа начинает работать(делает функцию сервера main))))
    web_ttit_proj()