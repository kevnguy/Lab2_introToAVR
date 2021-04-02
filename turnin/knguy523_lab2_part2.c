/*	Author: Kevin Nguyen  knguy523@ucr.edu
 *  Partner(s) Name: 
 *	Lab Section: 22
 *	Assignment: Lab #2  Exercise #2
 *	Exercise Description: Port A's pins 3 to 0, each connect to a parking space sensor, 1 meaning a car is parked 
 *		in the space, of a four-space parking lot. Write a program that outputs in binary on
 *		port C the number of available spaces
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
	DDRA = 0x00; PORTA = 0xFF;
	DDRC = 0xFF; PORTC = 0x00;
	
	unsigned A0, A1, A2, A3, count = 0x00;
		/* Insert your solution below */
    while (1) {
	count = 0;
	A0 = (PINA & 0x01);
	A1 = (PINA & 0x02) >> 1;
	A2 = (PINA & 0x04) >> 2;
	A3 = (PINA & 0x08) >> 3;
	count = A0 + A1 + A2 + A3;

	if(count < 4)
		count = 4 - count;
	else
		count = 0;
	PORTC = count;
    }
    return 1;
}
