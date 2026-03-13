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

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f" [v] Dapur Menerima Pesanan #{data['order_id']}: {data['menu']}")
    
    print(f"     Sedang memasak {data['menu']}...")
    
    print(f" [OK] {data['menu']} siap diambil!")
    print("-" * 30)

channel.basic_consume(
    queue='order_queue',
    on_message_callback=callback,
    auto_ack=True
)

print(' [*] Dapur siap menerima pesanan. Tekan CTRL+C untuk keluar.')
channel.start_consuming()