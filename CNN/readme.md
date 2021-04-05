
A CNN is a deep learning algorithm which takes input image in the form of pixcels associated with weights and biases.
It takes inspiration from the function of neurons fround in mammalian brain.
Mechanism of Convolution :
It is used to extract the relevent feature from of the  image and remove the retendencies by passing it through filter. The input image can be seen as a matrix of pixcel values .Depending upon whether image is in grayscale or RGB the image is splitted into channels like in RGB image the image is splitted into three channels in red, blue, green and then passed through the filter.In grayscale image the pixcel values ranges from o to 255 depending upon the intensity where 0 is for black and 255 denotes white.
Let us take one example:


Image dimension:


![first_equation](https://latex.codecogs.com/gif.latex?n*n*n_%7Bc%7D)
 
 Filter dimension:
 
 ![first_equation](https://latex.codecogs.com/gif.latex?f*f*n_%7Bc%7D)
 
 Number of filters used:
 10
 then the dimension of the output image is given by:
 
 ![first_equation](https://latex.codecogs.com/gif.latex?%28n-f&plus;1%29*%28n-f&plus;1%29*10)
 
 Padding:
 
 It refers to the addition of extra rows and columns alon the border of the image.This is done to cater two needs :
 
 To avoid the loss of information along the corners of the image and to ensure no loss of image dur to shrinkage in furthef layers of CNN.If we apply padding to the above equation 
 the dimension of the output image is:
 
 ![first_formula](https://latex.codecogs.com/gif.latex?%28n%20&plus;%202p%20-f%20&plus;1%29*%28n%20&plus;%202p%20-%20f%20&plus;1%29*10)
 where p is the number of layer of padding.
 
 Strided convolution:
  It is the extra shift of the filter over the image for example a strid of value 2 means that the filter will shift two rows/columns in each consequtive computation of the pixel values.Let us suppose we apply s stride in the above example so the dimension of the outpot image is givrn by:
  
  ![first_formula](https://latex.codecogs.com/gif.latex?%28%28n%20&plus;%202p%20-f%29/s%20&plus;1%29*%28%28n%20&plus;%202p%20-%20f%29/s%20&plus;1%29*10)
  
  Forward propagatiuon:
 After the image is passed through the filters, the pixcels values are multiplied by the weights and the bias is added and it is processed by the activation function, which in this case in the case is a rectified linear unit called ReLU function.If the input value is above a threshold quantity the node is activated . It works in such a way that the v negative value are rounded to 0 and the positive value remain as it is .
 
 Let us suppose we use a bias b and the associated weights :
 
 ![first_formula](https://latex.codecogs.com/gif.latex?h_%7Bw%7D%28x%29%3D%20x_%7B1%7Dw_%7B1%7D&plus;x_%7B2%7Dw_%7B2%7D.........x_%7Bn%7Dw_%7Bn%7D&plus;b)
 
 ![first_formula](https://latex.codecogs.com/gif.latex?a_%7Bj%7D%5E%7B%28L%29%7D%3D%5Csigma%20%28h_%7Bw%7D%28x%29%29)
 
 Backpropagation:
 
 It is very helpful to use backpropagation gor arriving it a desired value of weights and biases .For this we use a cost function and differenciate it with respect to the weight to observe how the cost is affected by small chages in weights and try to find the minimum of the cost function.
 
 Let y ne the target value , cost function is given by: 
 
 ![first_equation](https://latex.codecogs.com/gif.latex?C_%7Bo%7D%3D%5Csum_%7Bj%3D0%7D%5E%7Bn_%7Bl%7D-1%7D%28a_%7Bj%7D%5E%7B%28L%29%7D-y_%7Bj%7D%29%5E%7B2%7D)
 
 after differenciating it with respect to w and applying chain rule:
 
 ![first_equation](https://latex.codecogs.com/gif.latex?C_%7Bo%7D%7B%7D%27%3D%20a%5E%7B%28L-1%29%7D%5Csigma%7B%7D%27%28h_%7Bw%7D%28x%29%292%28a%5E%7B%28l%29%7D-y%29)
 
 
 
 sources:
 
 https://www.youtube.com/watch?v=Ilg3gGewQ5U&t=495s
