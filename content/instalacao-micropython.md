Title: Micropython
Date: 2020-04-05 09:00
Modified: 2020-04-05 09:00
Category: Microcontroladores
Tags: microcontroladores, python
Slug: instalacao-micropython

Já pensou em executar códigos python em seu ESP8266/ESP32? Com micropython isso é possível.

O micropython reescreve o firmware que executa códigos em C no seu ESP8266/ESP32 (entre outras boards), assim você pode escrever seus programas em python sem a preocupação de ter uma IDE ou compilação de código entre diferentes boards. Quase que em 90% dos casos o mesmo código escrito no ESP8266 irão executar no ESP32 (apesar de suas particularidades como executar threads, disponível apenas no ESP32).

### Instalação

Para realizar a instalação precisamos do pacote esptool que pode ser baixado pelo `pip3`:

    :::bash
    pip3 install esptool --user

Conecte seu ESP8266 ou ESP32 na porta usb do seu computador e execute o seguinte comando:

Este comando irá limpar a memória flash do seu ESP8266/ESP32:  
_A porta pode não ser igual a utilizada neste post._

    :::bash
    esptool.py --port /dev/ttyUSB0 erase_flash

Baixe a imagem oficial para sua board sendo ela o ESP8266 ou ESP32:

As imagens podem ser baixadas através do site: [https://micropython.org/download](https://micropython.org/download).

ESP8266:  
[https://micropython.org/resources/firmware/esp8266-20191220-v1.12.bin](https://micropython.org/resources/firmware/esp8266-20191220-v1.12.bin).  
ESP32:  
[https://micropython.org/resources/firmware/esp32-idf4-20191220-v1.12.bin](https://micropython.org/resources/firmware/esp32-idf4-20191220-v1.12.bin).  

_Links atualizados em 05/01/2020_

Para realizar o flash do firmware em seu ESP, execute o segundo comando:  
- _A porta pode não ser igual a utilizada neste post._  
- _O último parâmetro repassado no comando deve ser o nome do arquivo que você baixou._

    :::bash
    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190529-v1.11.bin

Após esses passos o firmware estará instalado no seu ESP8266/ESP32.  
Caso queria voltar a executar códigos em C na sua board, basta realizar qualquer upload através do Arduino IDE que o firmware original será reescrito novamente.

Fonte: [https://docs.micropython.org/en/latest/index.html](https://docs.micropython.org/en/latest/index.html)