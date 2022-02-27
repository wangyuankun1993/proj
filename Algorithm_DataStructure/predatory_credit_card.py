# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: predatory_credit_card.py
# Date: 2022/01/31 23:34:44
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from credit_card import CreditCard

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Crate a new predatory credit card instance
        apr annual percentage rate
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """
        Return False and access $5 fee if charge is denied.
        """
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Access monthly interest on outstanding balance."""
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
