import requests as req


def main():
    reply = req.get('https://reqres.in/api/users/2')
    print(f'reply: {reply.status_code}')
    print(f'200 OK? {reply.status_code == req.codes.ok} {reply.ok}')
    print(f'headers: {reply.headers}')
    print()
    print(f'content: {reply.content}')
    print()
    print(f'JSON content: {reply.json()}')

    print('-' * 100)

    try:
        reply = req.get('https://reqres.in/api_error/users/2')
    except req.RequestException:
        print('Communication Error')
    else:
        if reply.ok:
            print(f'JSON content: {reply.json()}')
        else:
            print('Server Error')

if __name__ == '__main__':
    main()
