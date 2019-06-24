#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Car():
    
    """A simple attempt to represent a car."""
    
    def __init__(self,make,model,year):
        
        """Intialize attributes to describe a car."""
        
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        
        """Return a neatly formated descriptive name."""
        
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading) + " milies on it.")
        
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        
    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
    def fill_gas_tank(self):
        print("Kindly fill your gas tank!")
    


# In[3]:


class Electriccar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70
        
    def describe_battery(self):
        print("This car has a " +str(self.battery_size) + "-kwh battery.")
        
    def fill_gas_tank(self):
        print("This car doesn,t need a gas tank!")


# In[ ]:


class Battery():
    def __init__(self,manufacture,cycles,amperes,battery_size=70):
        """Intialize the battery's attributes."""
        self.battery_size = battery_size
        self.manufacture = manufacture
        self.cycles = cycles
        self.amperes = amperes
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = 0
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = " This car go approxmiately " + str(range)
        message += " miles on a full charge."
        print(message)

