import time
from netmiko import ConnectHandler

router_parameter ={
    'device_type': 'cisco_ios',
    'host': '192.168.14.134',
    'username': 'admin',
    'password': 'admin',
    'secret': input("Current Password: ")
}

def get_new_enable_pwd():
    new_enable_password = input("Enter a new enable password: ")
    return new_enable_password
def change_enable_pwd(router_parameter, new_enable_password):
    try:
        with ConnectHandler(**router_parameter) as ssh:
            ssh.enable()
            ssh.send_config_set([f'enable secret {new_enable_password}'])
            print(f"Enable password changed successfully to: @{new_enable_password}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__=="__main__":
    while True:
        new_enable_password = get_new_enable_pwd()
        change_enable_pwd(router_parameter, new_enable_password)
        print("Waiting for a week before changing the enable password again...")
        time.sleep(604800)
