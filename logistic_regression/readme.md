# logistic_regression
Regression deals with a predictive modelling technique. It shows the relation between independent also known as predictive variable or dependent or target value.
Logistic regression comes int ouse when output is of categorical format such as yes/no , 1 or 0,true or false, high or low.
As in linear regression we get output values over a large range but for the categorical output it should be between 1 and 0, hence the linear regression curve is to be clipped between 1 and o which is performed using logistic regression , for this we use a sigmoid function.

![first equation](https://latex.codecogs.com/gif.latex?1/1%20&plus;%20e%5E%7B-h_%7B%5Cbeta%20%7D%28x%29%7D)


concept of threshold:
This is used to decide whether the output value(betwwen o and 1) rounds off to give the output as 0(low) or 1(high).
The output values between threshold value(0.5) and 1 is rounded to 1 and the value below threshold and is rounded to 0.

concept of log likelihood:
Using the concept of linear regression:

![first equation](https://latex.codecogs.com/gif.latex?h_%7B%5Cbeta%20%7D%28x%29%3D%20%5Cbeta%20_%7B1%7Dx_%7B1%7D&plus;%5Cbeta%20_%7B2%7Dx_%7B2%7D.....%5Cbeta%20_%7Bn%7Dx_%7Bn%7D)


putting the above value in sigmoid equation:


Now , by taking inspiration from Bernaulli's traits, we find the log likelyhood function and differentiating it to find the gradient ascent update equation. Hence the likelihood is defined as :

![first equation](https://latex.codecogs.com/gif.latex?l%28%5Cbeta%20%29%20%3D%20%5Cprod%20%28h%28x_%7B%5Cbeta%20%7D%29%29%5E%7By%7D%281%20-%20h%28x_%7Bb%7D%29%29%5E%7B1-y%7D)


log likelihood becomes:


![first equation](https://latex.codecogs.com/gif.latex?LL%28%5Cbeta%20%29%20%3D%20%5Csum%20ylog%28h_%7B%5Cbeta%20%7D%28x%29%29&plus;%281-y%29log%281-h_%7B%5Cbeta%20%7D%28x%29%29)


differenciating it:


![first equation](https://latex.codecogs.com/gif.latex?%5CDelta%20_%7B%5Cbeta%20%7DLL%28%5Cbeta%20%29%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7BN%7D%28%28y%20-%20h_%7B%5Cbeta%20%7D%28x%29%29X%5E%7B_%7B%5E%7B_%7Bi%7D%7D%7D%7D%29/N)


The gradient ascent update equation becomes:

![first equation](https://latex.codecogs.com/gif.latex?%5Cbeta%20%5Cleftarrow%20%5Cbeta%20&plus;%5Calpha%20%5CDelta%20_%7B%5Cbeta%20%7DLL%28%5Cbeta%20%29)

    
      logistic regression                                                                 linear regression
      categorical variable                                                                continuous variable
      solve classification problem                                                        solve regression problems
      Straight line graph                                                                 uses sigmoid graph
      
      Uses of logistic regression:
      used for weather forcast such as whether it is clound or ot will rain or not
      multiclass classification
      medical use like diagnosis of various disease.

