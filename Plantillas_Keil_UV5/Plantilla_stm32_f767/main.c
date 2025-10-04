
#include <stm32f767xx.h>

// Funcion de perdida de tiempo
void delay_ms(uint16_t n);

int main()
{
	// Configuracion de reloj

	// Configuracion de modo de puerto
	
	while(1)
	{
		delay_ms(200);
	}
}

void delay_ms(uint16_t n)
{
	uint16_t i, j;
	for(i=0; i<n; i++)
	{
		for(j=0; j<2000; j++);
	}
}