#Drawing Outlines of a RGB Image

The simple idea of taking differences between adjacent values is used here. We incorporate the concept of max pooling as well to reduce noise and unwanted fluctuations in the outlines. 

Initially, we carry out max pooling of each layer (R,G,B) to eliminate unwanted fluctuations and noise. Next we find the differences along the first and second dimensions. This gives us data about the sudden changes of colour, or in other words the edges. Next we carry out max pooling again to add extra weight to the discovered edges. 

Finally, we filter off the minor fluctuations again by removing differences below a particular set value. 

This final image gives us a reasonable approximation of outlines of the image. 