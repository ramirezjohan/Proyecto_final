
#include <MK20D5.h>

void delayMs(int n);

int main()
{
	/* Habilitacion del reloj de GPIOC */
	SIM->SCGC5 |= (1<<9);
	SIM->SCGC5 |= (1<<11);
	SIM->SCGC5 |= (1<<12);
	
	/* Configuracion del pin como GPIO*/
	PORTC->PCR[2] = PORT_PCR_MUX(1);
	PORTC->PCR[3] = PORT_PCR_MUX(1); 
	PORTD->PCR[4] = PORT_PCR_MUX(1);
	
	/* Establecer el GPIO como salida*/
	PTA->PDDR |= (1u << 2);
	PTC->PDDR |= (1u << 3);
	PTD->PDDR |= (1u << 4);
	
	/* Apagar los que no son necesarios */
	PTC->PDOR |= (1 << 3);
	PTD->PDOR |= (1 << 4);
	PTA->PDOR |= (1 << 2);
	
	while(1)
	{
		PTD->PTOR ^= (1<<4);
		delayMs(100);
	}
}

void delayMs(int n)
{
	int i, j;
	for(i=0; i<n; i++)
	{
		for(j=0; j<7000; j++);
	}
}