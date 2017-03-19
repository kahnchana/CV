function [ output_args ] = outline( x,z2,z1,y )
%sketches outline of image
%   uses differences along x and y axes to sketch outline. x=max diff,
%   y=times to diff, z1=max pooling square size, z2= times to max pool
%   z3=initial max pooling

if nargin<4
    y=1;
end

if nargin<3
    z1=2;
end

R=imread('Penguins.jpg');
R1=R;
z3=3;
R = cat(3,ordfilt2(R(:,:,1),z3^2,ones(z3,z3)),ordfilt2(R(:,:,2),z3^2,ones(z3,z3)),ordfilt2(R(:,:,2),z3^2,ones(z3,z3)));

a=abs(diff(R,y,1));
b=abs(diff(R,y,2));

a=cat(1,a,zeros(y,size(R,2),size(R,3)));
b=cat(2,b,zeros(size(R,1),y,size(R,3)));

for i=1:z2
    a = cat(3,ordfilt2(a(:,:,1),z1^2,ones(z1,z1)),ordfilt2(a(:,:,2),z1^2,ones(z1,z1)),ordfilt2(a(:,:,2),z1^2,ones(z1,z1)));
    b = cat(3,ordfilt2(b(:,:,1),z1^2,ones(z1,z1)),ordfilt2(b(:,:,2),z1^2,ones(z1,z1)),ordfilt2(b(:,:,2),z1^2,ones(z1,z1)));
end

c=a+b;
d=(abs(c)>x);
d=sum(d,3);
d=(d>0)*255;
clear a;
clear b;
clear c;

figure;
close all;
subplot(1,2,1);
imshow(R1)
subplot(1,2,2);
imshow(d)

end

