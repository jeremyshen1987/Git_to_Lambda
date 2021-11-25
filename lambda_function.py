def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['First_Name'], event['Last_Name'])  
    return { 
        'message' : message
        print('Done!')
    }