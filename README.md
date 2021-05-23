# Reto Módulo 3:
Sistema de apoyo a la vacunación rural

## Objetivo

- El sistema debe proveer un módulo de registro en el cual se deben registrar los datos básicos para poder realizar el cálculo de la fecha de la cita. (se debe hacer con una función)
- Al momento de finalizar el registro el sistema debe generar una clave constituida de la siguiente manera: primeras dos letras del primer nombre, primeras dos letras del primer apellido y número de cédula, esta clave debe ser utilizada para ingresar al módulo de asignación de citas. (debe crear una función que genere la clave)
- El sistema debe proveer un módulo de inicio que valide el acceso a la asignación de citas sólo si la clave generada anteriormente y la cédula corresponden a una misma persona. (se debe hacer con una función)
- Con base en todos los parámetros asignados el sistema de entregar la fecha de la cita en la cual será vacunado el paciente. (se debe realizar con una función)
- Adicionalmente deben existir funciones que permitan validar si un número es primo, otro que entregue la edad de una persona en años, meses y días, es importante tener en cuenta que el tipo de sangre se debe validad en mayúscula, aunque el usuario lo ingrese en minúscula.
- Para solucionar el reto puede utilizar funciones creadas por usted mismo, o algunas que ya existan definidas en el lenguaje de programación y las pueda adaptar al presente contexto.

## Descripción del Ret 

En el centro de salud MiVereda, necesitan establecer un proceso para la asignación de turnos de vacunación contra el Covid-19; cómo la cantidad de vacunas que se tiene en existencia no permite realizar jornadas masivas, la dirección del centro de salud ha definido algunos parámetros que permitan priorizar la aplicación de la vacuna a las personas más vulnerables, los parámetros son los siguientes:

- Mujeres mayores de 60 años, con tipo de sangre 0+, con un peso mayor a 70 kilos y que los dos últimos números de su cédula constituyan un numero primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/150), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- Mujeres mayores de 60 años, con tipo de sangre 0+, con un peso mayor a 70 kilos y que los dos últimos números de su cédula constituyan un número no primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/80), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- Mujeres mayores de 60 años, con tipo de sangre A-, con un peso mayor a 70 kilos y que los dos últimos números de su cédula constituyan un numero primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/200), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- Mujeres mayores de 60 años, con tipo de sangre A-, con un peso mayor a 70 kilos y que los dos últimos números de su cédula constituyan un número no primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/45), es importante tener en cuenta que la edad de una persona se representa en años, meses y días 

- Mujeres mayores de 60 años, con tipo de sangre diferente a 0+ y A-, con un peso mayor a 70 kilos y que los dos últimos números de su cédula constituyan un numero primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/175), es importante tener en cuenta que la edad de una persona se representa en años, meses y días.

- Todas las mujeres mayores de 60 años que tengan un peso menor a 70 kilos se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/100), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- Hombres mayores de 60 años, con tipo de sangre 0+, con un peso mayor a 80 kilos y que los dos últimos números de su cédula constituyan un numero primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/180), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- Hombres mayores de 60 años, con tipo de sangre 0+, con un peso mayor a 80 kilos y que los dos últimos números de su cédula constituyan un número no primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/90), es importante tener en cuenta que la edad de una persona se representa en años, meses y días 

- Hombres mayores de 60 años, con tipo de sangre A-, con un peso mayor a 80 kilos y que los dos últimos números de su cédula constituyan un numero primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/210), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- Hombres mayores de 60 años, con tipo de sangre A-, con un peso mayor a 80 kilos y que los dos últimos números de su cédula constituyan un número no primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/40), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- Hombres mayores de 60 años, con tipo de sangre diferente a 0+ y A-, con un peso mayor a 80 kilos y que los dos últimos números de su cédula constituyan un numero primo, se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/145), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- Todos los hombres mayores de 60 años que tengan un peso menor a 80 kilos se les asignará la cita para una fecha que se calcula de la siguiente manera: fechaCita=fechaRegistro+(edad persona en días/105), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- A todas las personas menores de 60 se les asignará la cita con la siguiente formula fechaCita=fechaRegistro+(edad persona en días/250), es importante tener en cuenta que la edad de una persona se representa en años, meses y días

- Para todos los casos el sistema de decir: su cita será en x meses y x días

### Aspectos a tener en cuenta 

- El sistema debe proveer un módulo de registro en el cual se deben registrar los datos básicos para poder realizar el cálculo de la fecha de la cita. (se debe hacer con una función)

- Al momento de finalizar el registro el sistema debe generar una clave constituida de la siguiente manera: primeras dos letras del primer nombre, primeras dos letras del primer apellido y número de cédula, esta clave debe ser utilizada para ingresar al módulo de asignación de citas. (debe crear una función que genere la clave)

- El sistema debe proveer un módulo de inicio que valide el acceso a la asignación de citas sólo si la clave generada anteriormente y la cédula corresponden a una misma persona. (se debe hacer con una función)

- Con base en todos los parámetros asignados el sistema de entregar la fecha de la cita en la cual será vacunado el paciente. (se debe realizar con una función)

- Adicionalmente deben existir funciones que permitan validar si un número es primo, otro que entregue la edad de una persona en años, meses y días, es importante tener en cuenta que el tipo de sangre se debe validad en mayúscula, aunque el usuario lo ingrese en minúscula.

- Para solucionar el reto puede utilizar funciones creadas por usted mismo, o algunas que ya existan definidas en el lenguaje de programación y las pueda adaptar al presente contexto.