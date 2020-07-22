{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Program to check if a number is prime or not\n",
    "\n",
    "num = 407\n",
    "\n",
    "# To take input from the user\n",
    "#num = int(input(\"Enter a number: \"))\n",
    "\n",
    "# prime numbers are greater than 1\n",
    "if num > 1:\n",
    "   # check for factors\n",
    "   for i in range(2,num):\n",
    "       if (num % i) == 0:\n",
    "           print(num,\"is not a prime number\")\n",
    "           print(i,\"times\",num//i,\"is\",num)\n",
    "           break\n",
    "   else:\n",
    "       print(num,\"is a prime number\")\n",
    "       \n",
    "# if input number is less than\n",
    "# or equal to 1, it is not prime\n",
    "else:\n",
    "   print(num,\"is not a prime number\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
