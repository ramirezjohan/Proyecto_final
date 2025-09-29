
class BaseAdapter:
    def generate_code(self, peripheral):
        raise NotImplementedError("El adaptador debe implementar generate_code()")
