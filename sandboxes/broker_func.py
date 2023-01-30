from tinkoff.invest import Client
from tinkoff.invest.services import SandboxService
import tokens



def get_all_accounts():
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.get_sandbox_accounts().accounts

        [print(acc) for acc in r]


def get_id_accounts():
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.get_sandbox_accounts().accounts

        [print(acc.id) for acc in r]

def create_account():
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.open_sandbox_account()

        return print(r)


if __name__ == '__main__':
    get_id_accounts()
#     create_account()