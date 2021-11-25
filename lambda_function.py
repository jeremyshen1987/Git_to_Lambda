def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['First_name'], event['Last_name'])  
    return { 
        'message' : message
    }