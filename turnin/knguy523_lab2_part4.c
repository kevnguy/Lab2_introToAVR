/*	Author: Kevin Nguyen  knguy523@ucr.edu
 *  Partner(s) Name: 
 *	Lab Section: 22
 *	Assignment: Lab #2  Exercise #4
 *	Exercise Description: An amusement park kid ride cart has three seats, with 8-bit weight sensors connected to 
 *		ports A, B, and C (measuring from 0-255 kilograms). Set PD0 to 1 if the cart's total passenger
 *		weight exceeds the maximum of 140 kg. Also, the cart must be balanced: Set port PD1 to 1 if the 
 *		difference between A and C exceeds 80 kg.  The remaining 6 bits on D should display an 
 *		approximation of the total combined weight
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
	DDRB = 0x00; PORTB = 0xFF;
	DDRC = 0x00; PORTC = 0xFF;
	DDRD = 0xFF; PORTD = 0x00;
	
	unsigned weightA, weightB, weightC, weightT = 0x00;
		/* Insert your solution below */
    while (1) {
	weightT = 0;
	PORTD = 0x00;
	weightA = PINA;
	weightB = PINB;
	weightC = PINC;
	weightT = weightA + weightB + weightC;
	if(weightT > 0x8C) // 140
		PORTD = 0x01;
	if((weightA - weightC > 0) && (weightA - weightC > 0x50)) // 80
		PORTD |= 0x02;
	else if((weightC - weightA > 0) && (weightC - weightA> 0x50))
		PORTD |= 0x02;
/*
	if(weightT <= 0x20) 
		weightT <<= 2;
	else if(weightT <= 0x40);
		weightT <<= 1;
*/
	
	weightT &= 0xFC;	
	PORTD |= weightT;
    }
    return 1;
}
