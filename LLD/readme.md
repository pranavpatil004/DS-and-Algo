#LLD Cheatsheet:

##Creational Patterns:

Markup :    1. Factory
                -- usefull when we want to "externalize object creation."
                -- create a factory class which contains a method which returns the given object.
                -- eg. Cars: ford-fusion, chevy-volt, jeep-sahara. Create a factory which will return objects of these classes based on the enum or name provided.
            2. Abstract Factory
                -- usefull when there is a family of classes we want to instantiate.
                -- create an abstract factory class which will be inherited by different individual factories and implement their own implementations.
                -- eg. different types of cars: economy, sport, luxury etc. Create an abstract factory which will have methods to create economy, sport and luxury cars. Different manufacturers like Ford, and GM will implement their own implementations of these methods. Eg. Ford will return fusion for their economy method, and GM will return something else. 
            3. Builder
                -- useful when the object needs multiple parameters for its creation.
                -- also useful when we want to force a specific order while creating the object.
                -- It has an abstract builder and its implementations. It has a director class which actually calls the builder classes and get the objects built in a specific order. You use the director in your code to get the object created. If an object has different sequences, then you can have different directors.
                -- eg. JIRA utility class
                -- eg. Computer class: create a builder which will take the inputs from user and create the object in a desired order and then return the object.
            4. Prototype:
                -- create a single class(prototype) and implement similar other classes as runtime inheritance.The prototype class implements a clone method which is called whenever we want to create a new object. After the object is created/cloned, we change the values of the new object.
                -- Deep copy should be used whenever we have objects within objects and we want to ensure that the embedded objects are also cloned.
                -- Shallow copy can be used when we have only the basic datatypes.
                -- Prototype manager can be used for prototype creation.
                -- Implementation: TODO

##Structural Patterns:
Markup :    1. Adapter:
                -- two types: Object adapters: Composition, Class adapters: Inheritance
                i. Client: Class or object who is using the services.
                ii. Adaptee: The new API or class whose interface is not compatible with existing code.
                iii. Adapter: Class which makes Adaptee's interface compatible with the existing code so that the client can use it.
                iv. Target: Domain-specific interface used currently by the client.
