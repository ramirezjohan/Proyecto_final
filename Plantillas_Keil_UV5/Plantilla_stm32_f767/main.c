
#include <stm32f767xx.h>
void delay_ms(uint16_t n);

int main()
{
	RCC->AHB1ENR |= (1 << 1);
	
	GPIOB->MODER &= ~(3 << (7*2));
  GPIOB->MODER |=  (1 << (7*2));
	
	while(1)
	{
		GPIOB->ODR ^= (1 << 7);
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