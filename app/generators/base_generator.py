
class BaseGenerator:
    def generate(self, mcu, peripherals):
        raise NotImplementedError("Debe implementarse en la subclase")
