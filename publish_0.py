import paho.mqtt.client as mqtt
import json
import threading


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

class Publish_0(threading.Thread):

    #-------------------------0
    client_0 = mqtt.Client()
    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
    client_0.on_connect = on_connect
    client_0.on_disconnect = on_disconnect
    client_0.on_publish = on_publish
    # address : localhost, port: 1883 에 연결
    client_0.connect('192.168.0.101', 1883)
    client_0.loop_start()

    # #-------------------------1
    client_1 = mqtt.Client()
    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
    client_1.on_connect = on_connect
    client_1.on_disconnect = on_disconnect
    client_1.on_publish = on_publish
    # address : localhost, port: 1883 에 연결
    client_1.connect('192.168.0.101', 1883)
    client_1.loop_start()
    # #-----------------------------------2
    client_2 = mqtt.Client()
    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
    client_2.on_connect = on_connect
    client_2.on_disconnect = on_disconnect
    client_2.on_publish = on_publish
    # address : localhost, port: 1883 에 연결
    client_2.connect('192.168.0.101', 1883)
    client_2.loop_start()
    #
    # # -----------------------------------3
    client_3 = mqtt.Client()

    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
    client_3.on_connect = on_connect
    client_3.on_disconnect = on_disconnect
    client_3.on_publish = on_publish
    # address : localhost, port: 1883 에 연결
    client_3.connect('192.168.0.101', 1883)
    client_3.loop_start()
    # #-----------------------------------4
    client_4 = mqtt.Client()

    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
    client_4.on_connect = on_connect
    client_4.on_disconnect = on_disconnect
    client_4.on_publish = on_publish
    # address : localhost, port: 1883 에 연결
    client_4.connect('192.168.0.101', 1883)
    client_4.loop_start()
    #
    # #----------------------------------5
    client_5 = mqtt.Client()


    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
    client_5.on_connect = on_connect
    client_5.on_disconnect = on_disconnect
    client_5.on_publish = on_publish
    # address : localhost, port: 1883 에 연결
    client_5.connect('192.168.0.101', 1883)
    client_5.loop_start()
    #
    # # -----------------------------6
    client_6 = mqtt.Client()


    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
    client_6.on_connect = on_connect
    client_6.on_disconnect = on_disconnect
    client_6.on_publish = on_publish
    # address : localhost, port: 1883 에 연결
    client_6.connect('192.168.0.101', 1883)
    client_6.loop_start()

    while True:
        # 새로운 클라이언트 생성

        # common topic 으로 메세지 발행
        client_0.publish('testtopic', json.dumps({"success": "anyractive"}), 1)
        client_0.publish('testtopic', json.dumps({"success": "anyractive_11"}), 1)
        client_0.publish('testtopic', json.dumps({"success": "anyractive"}), 1)
        client_0.publish('testtopic', json.dumps({"success": "anyractive_11"}), 1)

        client_1.publish('testtopic', json.dumps({"success": "anyractive"}), 1)
        client_1.publish('testtopic', json.dumps({"success": "anyractive_11"}), 1)
        client_1.publish('testtopic', json.dumps({"success": "anyractive_22"}), 1)
        client_1.publish('testtopic', json.dumps({"success": "anyractive_33"}), 1)
        #
        client_2.publish('testtopic', json.dumps({"success": "anyractive"}), 1)
        client_2.publish('testtopic', json.dumps({"success": "anyractive_11"}), 1)
        client_2.publish('testtopic', json.dumps({"success": "anyractive_22"}), 1)
        client_2.publish('testtopic', json.dumps({"success": "anyractive_33"}), 1)
        #
        client_3.publish('testtopic', json.dumps({"success": "anyractive"}), 1)
        client_3.publish('testtopic', json.dumps({"success": "anyractive_11"}), 1)
        client_3.publish('testtopic', json.dumps({"success": "anyractive_22"}), 1)
        client_3.publish('testtopic', json.dumps({"success": "anyractive_33"}), 1)
        #
        #
        client_4.publish('testtopic', json.dumps({"success": "anyractive"}), 1)
        client_4.publish('testtopic', json.dumps({"success": "anyractive_11"}), 1)
        client_4.publish('testtopic', json.dumps({"success": "anyractive_22"}), 1)
        client_4.publish('testtopic', json.dumps({"success": "anyractive_33"}), 1)


        client_5.publish('testtopic', json.dumps({"success": "anyractive"}), 1)
        client_5.publish('testtopic', json.dumps({"success": "anyractive_11"}), 1)
        client_5.publish('testtopic', json.dumps({"success": "anyractive_22"}), 1)
        client_5.publish('testtopic', json.dumps({"success": "anyractive_33"}), 1)


        client_6.publish('testtopic', json.dumps({"success": "anyractive"}), 1)
        client_6.publish('testtopic', json.dumps({"success": "anyractive_11"}), 1)
        client_6.publish('testtopic', json.dumps({"success": "anyractive_22"}), 1)
        client_6.publish('testtopic', json.dumps({"success": "anyractive_33"}), 1)

        #client.loop_stop()
        # 연결 종료
        #client.disconnect()