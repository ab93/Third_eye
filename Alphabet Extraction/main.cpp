#include <iostream>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <opencv2/opencv.hpp>
#include <vector>
#include<stdio.h>


using namespace std;
using namespace cv;

int main()
{
    int c=0;
    VideoCapture cap(0);
    if (!cap.isOpened())  //check if video device has been initialised
    {    cout << "cannot open camera";}

    //namedWindow("Video",CV_WINDOW_AUTOSIZE);
int    flag = 0;
cout<<"enter the value:";
cin>>flag;
if (flag==1){

    Mat imgTmp;
    Mat resized;
    cap.read(imgTmp);
    Mat imgLines = Mat::zeros( imgTmp.size(), CV_8UC3);;
CvMoments omoments;
static int posX, posY ;
    while(true) {
    Mat cameraFrame;
cap.read(cameraFrame);
//imshow("cam", cameraFrame);
         Mat imgHSV;

cvtColor(cameraFrame, imgHSV, COLOR_BGR2HSV); //Convert the captured frame from BGR to HSV
//imshow("convert", imgHSV);
Mat imgThresholded;

//inRange(imgHSV, Scalar(155,120,110), Scalar(165, 162, 173), imgThresholded); //Threshold the image
//inRange(imgHSV, Scalar(102,180,190), Scalar(110, 225, 230), imgThresholded);
inRange(imgHSV, Scalar(100,200,60), Scalar(115, 255, 160), imgThresholded);
//morphological opening (remove small objects from the foreground)
erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );
dilate( imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );

//morphological closing (fill small holes in the foreground)
dilate( imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );
erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );

//imshow("Thresholded Image", imgThresholded); //show the thresholded image
//imshow("Original", frame); //show the original image
 //Calculate the moments of the thresholded image
omoments=moments(imgThresholded);
 double moment10 = cvGetSpatialMoment(&omoments, 1, 0); //Sum of X coordinates of all white pixels
double moment01 = cvGetSpatialMoment(&omoments, 0, 1); //Sum of Y coordinates of all white pixels
double area = cvGetCentralMoment(&omoments, 0, 0); //Sum of all white color pixels
 int iLastX = -1;
int iLastY = -1;
iLastX = posX;
iLastY = posY;
// if the area <= 10000, I consider that the there are no object in the image and it's because of the noise, the area is not zero
if (area > 1000)
{
//calculate the position of the ball
posX = moment10 / area;
posY = moment01 / area;

if (iLastX > 0 && iLastY > 0 && posX > 0 && posY > 0)
{
//Draw a red line from the previous point to the current point
line(imgLines, cvPoint(posX, posY), cvPoint(iLastX, iLastY), cvScalar(255,255,255), 8);
}

}
imshow("Thresholded Image", imgThresholded); //show the thresholded image

imshow("Original", imgLines); //show the original image

        c = cvWaitKey(20);
        if (c==27)
        break;
    }
//imwrite("/home/charvi/Documents/eye coding/thirdeye.png",imgLines);

std::vector<cv::Point> nonBlackList;
nonBlackList.reserve(imgLines.rows*imgLines.cols);
for(int j=0; j<imgLines.rows; ++j)
    for(int i=0; i<imgLines.cols; ++i)
    {
        // if not black: add to the list
        if(imgLines.at<cv::Vec3b>(j,i) != cv::Vec3b(0,0,0))
        {
            nonBlackList.push_back(cv::Point(i,j));
        }
    }
    cv::Rect bb = cv::boundingRect(nonBlackList);
    // display result and save it
cv::imshow("found rect", imgLines(bb));
cv::imwrite("CropWhiteResult.png", imgLines(bb));
cv::resize(imgLines(bb),resized,cv::Size(900,1200));
imwrite("/home/yuvraj/Documents/project/final3rdeye/yuvi.png",resized);
 Mat img;
   // int i; int j;
    img= imread("/home/yuvraj/Documents/project/final3rdeye/yuvi.png",1);
    Mat block1= img(Rect(0,0,300,300));
    Mat block2= img(Rect(0,300,300,300));
    Mat block3= img(Rect(0,600,300,300));
    Mat block4= img(Rect(0,900,300,300));
    Mat block5= img(Rect(300,0,300,300));
    Mat block6= img(Rect(300,300,300,300));
    Mat block7= img(Rect(300,600,300,300));
    Mat block8= img(Rect(300,900,300,300));
    Mat block9= img(Rect(600,0,300,300));
    Mat block10= img(Rect(600,300,300,300));
    Mat block11= img(Rect(600,600,300,300));
    Mat block12= img(Rect(600,900,300,300));
    imshow("block1",block1);
    imshow("block2",block2);
    imshow("block3",block3);
    imshow("block4",block4);
    imshow("block5",block5);
    imshow("block6",block6);
    imshow("block7",block7);
    imshow("block8",block8);
    imshow("block9",block9);
    imshow("block10",block10);
    imshow("block11",block11);
    imshow("block12",block12);
//int b;
//Mat channel[3];
//split(block12,channel);
vector<Mat> rgb[12];
//imshow("channel",channel)

//rgb[0].push_back( Mat(block8.rows, block8.cols, CV_8UC1));
rgb[0].push_back( Mat(block1.rows, block1.cols, CV_8UC1));
//rgb[0].push_back( Mat(block8.rows, block8.cols, CV_8UC1));
//rgb[0].push_back( Mat(block8.rows, block8.cols, CV_8UC1));
split(block1,rgb[0]);
//imshow("red", rgb[0].at(2));
//imshow("green", rgb[0].at(1));
//imshow("blue", rgb[0].at(0));
int b1=countNonZero(rgb[0].at(0));
//int w=countNonZero(rgb[].at(1));
rgb[1].push_back( Mat(block2.rows, block2.cols, CV_8UC1));
split(block2,rgb[0]);
int b2=countNonZero(rgb[1].at(0));

rgb[2].push_back( Mat(block3.rows, block3.cols, CV_8UC1));
split(block3,rgb[2]);
int b3=countNonZero(rgb[2].at(0));

rgb[3].push_back( Mat(block4.rows, block4.cols, CV_8UC1));
split(block4,rgb[3]);
int b4=countNonZero(rgb[3].at(0));

rgb[4].push_back( Mat(block5.rows, block5.cols, CV_8UC1));
split(block5,rgb[4]);
int b5=countNonZero(rgb[4].at(0));

rgb[5].push_back( Mat(block6.rows, block6.cols, CV_8UC1));
split(block6,rgb[5]);
int b6=countNonZero(rgb[5].at(0));

rgb[6].push_back( Mat(block7.rows, block7.cols, CV_8UC1));
split(block7,rgb[6]);
int b7=countNonZero(rgb[6].at(0));

rgb[7].push_back( Mat(block8.rows, block8.cols, CV_8UC1));
split(block8,rgb[7]);
int b8=countNonZero(rgb[7].at(0));

rgb[8].push_back( Mat(block9.rows, block9.cols, CV_8UC1));
split(block9,rgb[8]);
int b9=countNonZero(rgb[8].at(0));

rgb[9].push_back( Mat(block10.rows, block10.cols, CV_8UC1));
split(block10,rgb[9]);
int b10=countNonZero(rgb[9].at(0));

rgb[10].push_back( Mat(block11.rows, block11.cols, CV_8UC1));
split(block11,rgb[10]);
int b11=countNonZero(rgb[10].at(0));

rgb[11].push_back( Mat(block12.rows, block12.cols, CV_8UC1));
split(block12,rgb[0]);
int b12=countNonZero(rgb[11].at(0));
cout<<b1<<" "<<b2<<" "<<b3<<" "<<b4<<" "<<b5<<" "<<b6<<" "<<b7<<" "<<b8<<" "<<b9<<" "<<b10<<" "<<b11<<" "<<b12;

//Mat gesture;int rows=1; int cols=12;
//gesture=Mat::zeros(rows,cols,CV_8U);
int g[12]={b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12};

//for(i=0;i<12;i+i+1){
//gesture[0]= b1;
//gesture[1]= b2;
//gesture[2]= b3;
//gesture[3]= b4;
//gesture[4]= b5;
//gesture[5]= b6;
//gesture[6]= b7;
//gesture[7]= b8;
//gesture[8]= b9;
//gesture[9]= b10;
//gesture[10]= b11;
//gesture[11]= b12;

int k1[12];int k2[12];int k3[12];int l1[12];int l2[12];
k1[0]=18951; k1[1]=0; k1[2]=5750; k1[3]=12062; k1[4]=7272; k1[5]=21872; k1[6]=8171; k1[7]=0; k1[8]=16081;k1[9]= 20842;k1[10]= 19505;k1[11]= 0;
k2[0]=14313; k2[1]=0; k2[2]=1437; k2[3]=11473; k2[4]=15561; k2[5]=6052; k2[6]=10405; k2[7]=0; k2[8]=17205;k2[9]= 31823;k2[10]= 19756;k2[11]= 0;
k3[0]=12103; k3[1]=0; k3[2]=0; k3[3]=10502; k3[4]=9101; k3[5]=12864; k3[6]=9998; k3[7]=8381; k3[8]=17602;k3[9]= 37828;k3[10]= 36477;k3[11]= 0;
l1[0]=0; l1[1]=0; l1[2]=0; l1[3]=7616; l1[4]=0; l1[5]=0; l1[6]=0; l1[7]=7743; l1[8]=11263;l1[9]=5511;l1[10]= 5197;l1[11]= 0;
l2[0]=0; l2[1]=0; l2[2]=0; l2[3]=8548; l2[4]=0; l2[5]=0; l2[6]=0; l2[7]=7896; l2[8]=18339;l2[9]=6910;l2[10]= 6906;l2[11]= 0;
//cout<<gesture[0];
//cout<<gesture[0];
int K1[2]={abs(g[0]-k1[0]),abs(g[1]-k1[1])};
int qw;
qw= K1[0]+ K1[1];
int K2[12]; int K3[12]; int L1[12]; int L2[12];
//gesture
//absdiff(gesture, k1, K1);
//absdiff(gesture, k2, K2);
//absdiff(gesture, k3, K3);
//absdiff(gesture, l1, L1);
//absdiff(gesture, l2, L2);
//double s= sum(K1);
//cout<<s;


//b= countNonZero(block12[0]);
//cout<<b;


    waitKey(0);
   return 0;
   }
}




