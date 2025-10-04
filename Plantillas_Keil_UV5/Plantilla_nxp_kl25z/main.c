
#include <MKL25Z4.h>

void delayMs(int n);

int main()
{
	/* Habilitacion del reloj */
	SIM->SCGC5 |= (1<<10);
	
	/* Configurar en MUX como GPIO*/
	PORTB->PCR[18] = PORT_PCR_MUX(1);  /* PIN -> GPIO */
	
	/* Configurar el GPIO como salida*/
	GPIOB->PDDR |= (1u << 18);  /* configurar como salida */
	
	while(1)
	{
		GPIOB->PTOR ^= (1<<18);
		delayMs(100);
	}
}

// delay n milisegundos a 41.94MHz
void delayMs(int n)
{
    int i, j;
    for(i = 0 ; i < n; i++)
        for(j = 0; j < 7000; j++)
            {}
}
