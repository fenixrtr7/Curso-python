employeers = [
    {'name': 'Carlos', 'role': 'admin'},
    {'name': 'Juan', 'role': 'employee'},
    {'name': 'Jose', 'role': 'employee'},
    {'name': 'Ana', 'role': 'employee'}
]


def delete_employeer(employeers: list[dict], name_employeer: str):
    for employeer in employeers:
        if (employeer["name"] == name_employeer):
            employeers.remove(employeer)
            return True
    return False


def add_amployeer(employeers: list[dict], name: str, role: str):
    employeers.append({"name": name,"role": role})

if __name__ == "__main__":
    print(delete_employeer(employeers, "Juan"))
    print(employeers)
    add_amployeer(employeers, "Antonio", "admin")
    print(employeers)