import json
from datetime import datetime

def lambda_handler(event, context):
    # Obter a data e hora atual
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Imprimir a data atual
    print(f"Data e hora atual: {current_date}")
    
    # Retornar a data atual como resposta
    return {
        'statusCode': 200,
        'body': json.dumps(f'Data e hora atual: {current_date}')
    }
