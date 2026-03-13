import pika
import json

credentials = pika.PlainCredentials('cilla', 'cilla')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=credentials
    )
)
channel = connection.channel()

channel.queue_declare(queue='order_queue')

def send_order(order_id, menu):
    event_data = {
        "order_id": order_id,
        "menu": menu,
        "status": "DIPESAN"
    }
    message = json.dumps(event_data)
    
    channel.basic_publish(exchange='',
                          routing_key='order_queue',
                          body=message)
    print(f" [x] Event dikirim: {message}")

orders = ["Ayam Cr1sb4r", "Mie Ayam D4llas", "Pempek"]
for i, menu in enumerate(orders, 1):
    send_order(i, menu)

connection.close()