from Object import Discriminant


class ProxyCacheWithAccessControl:
    def __init__(self, dick: Discriminant):
        self.proxy_example = dick
        self._access_granted = False

    def access(self, access: int):
        if access == 1:
            self._access_granted = True

    def count(self, num_a: int, num_b: int, num_c: int):
        if not self._access_granted:
            print("Error")
            return None
        return self.proxy_example.count()


# Клиентский код
if __name__ == "__main__":
    proxy = ProxyCacheWithAccessControl(dick=Discriminant(num_a=1, num_b=5, num_c=4))
    proxy.access(access=1)
    print(proxy.count(num_a=1, num_b=5, num_c=4))
    print(proxy.count(num_a=1, num_b=5, num_c=4))
    proxy = ProxyCacheWithAccessControl(dick=Discriminant(num_a=1, num_b=-3, num_c=2))
    proxy.access(access=1)
    print(proxy.count(num_a=1, num_b=-3, num_c=2))# Выполняем вычисление
