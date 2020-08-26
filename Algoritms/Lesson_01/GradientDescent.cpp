//��������� ��� ������ �������� ������� ������� ������������ ������
#include<iostream>
#include<vector>
#include<math.h>

#define METHOD (2)
//����� ������ ����������� ����� ����
//1 - ����� ������������ ������ � ���������� �����
//2 - ����������� ����� � ���������� ����
//3 - ����� ������������� ������

//��������� ��� ������ ������������ ������ � ���������� �����
//��������� �������� eps ��� ������ � ���������� ����
#define LAMBDA_CONSTANT (1)

//��������� ��� ������ � ���������� ����
#define DELTA_FOR_METHOD2 (0.95)
#define EPS_FOR_METHOD2 (0.1)

//����������� ��������� ����� ��������
#define NUMBER_OF_ITERATIONS (100000)

//eps ��� �������� ��������
#define EPS (1e-5)

//�������� ��������
#define OSTANOV (2)

using namespace std;

vector<double> goldensectionoptimize(vector<double> x,double a, double b, int n);
double f(vector<double> x);
vector<double> GradientDescent(int N,vector<double> x0,int&Iterations);




double f(vector<double> x)
//������� ������� ������� ����
{
	//int l=x.size();
	//return (100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0])+(1-x[0])*(1-x[0]));
	return 10*x[0]*x[0]+x[1]*x[1];
}

vector<double> GradientF(vector<double> x)
//�������� ����������� �������
{
	vector<double> tmp;
	//tmp.push_back(-2*(1-x[0])-400*(x[1]-x[0]*x[0])*x[0]);
	//tmp.push_back(200*x[1]);
	tmp.push_back(20*x[0]);
	tmp.push_back(2*x[1]);
	return tmp;
}


vector<double> GradientDescent(int N,vector<double> x0,int&Iterations)
//minimizes N-dimensional function f; x0 - start point
{
	vector <double> old,cur_x=x0,gr;
	double s,Lambda;
	int j,i;

	Lambda=LAMBDA_CONSTANT;
	
	for (Iterations=1;Iterations<=NUMBER_OF_ITERATIONS;Iterations++)
	{
		//save old value
		old=cur_x;
		//compute gradient
        gr=GradientF(cur_x);
		

		if (METHOD==1)
		{

			Lambda=LAMBDA_CONSTANT;
			//��������� ����� ��������
			for(j=0;j<old.size();j++)
				cur_x[j]=cur_x[j]-Lambda*gr[j];
		}

		if (METHOD==2)
		{
			//��������� ����� ��������
			for(j=0;j<old.size();j++)
				cur_x[j]=cur_x[j]-Lambda*gr[j];

			//��������� ������� ����� ���������
			s=0;
			for(j=0;j<old.size();j++)
				s+=gr[j]*gr[j];


			while (f(cur_x)>f(old)-EPS_FOR_METHOD2*Lambda*s)
			{
				Lambda=Lambda*DELTA_FOR_METHOD2;
				//�������� �������� �����
				cur_x=old;
				for(j=0;j<old.size();j++)
					cur_x[j]=cur_x[j]-Lambda*gr[j];
			}
			
		}

		if (METHOD==3)
		{
			cur_x=goldensectionoptimize(cur_x,-10,10,100);
		}







		
		if(OSTANOV==1)
		{
			//������� �������� 1
			s=0;
			for(j=0;j<old.size();j++)
				s+=(old[j]-cur_x[j])*(old[j]-cur_x[j]);
			s=sqrt(s);
			if (s<EPS)
				return cur_x;
		}

		if(OSTANOV==2)
		{
			//������� �������� 2
			s=fabs(f(cur_x)-f(old));
			if (s<EPS)
				return	cur_x;
		}

	}

	return cur_x;
}

int main()
{
	vector<double> x;
	x.push_back(10);
	x.push_back(10);
	int i,Iteration;
	vector<double> ans=GradientDescent(2,x,Iteration);
	cout<<"Value: "<<f(ans)<<endl;
	cout<<"Point: ";
	for(i=0;i<ans.size();i++)
		cout<<ans[i]<<' ';
	cout<<endl<<"Number of iterations:"<<Iteration<<endl;
	return 0;
}

vector<double> goldensectionoptimize(vector<double> x,double a, double b, int n)
//����� �������� ������� ���������� ����������� ������� f
//������ ���������� x �� ������� [a,b], n ��������
//���� � ����� http://alglib.sources.ru/
{
	vector<double> tmp=x;
	int i,j;
    double s1;
    double s2;
    double u1;
    double u2;
    double fu1;
    double fu2;
	vector<double> GF=GradientF(x);

    s1 = (3-sqrt(double(5)))/2;
    s2 = (sqrt(double(5))-1)/2;
    u1 = a+s1*(b-a);
    u2 = a+s2*(b-a);
	
	for(j=0;j<x.size();j++)
		tmp[j]=x[j]+u1*GF[j];
	fu1 = f(tmp);
	
	for(j=0;j<x.size();j++)
		tmp[j]=x[j]+u2*GF[j];
	fu2 = f(tmp);

    for(i = 1; i <= n; i++)
    {
        if( fu1<=fu2 )
        {
            b = u2;
            u2 = u1;
            fu2 = fu1;
            u1 = a+s1*(b-a);
			for(j=0;j<x.size();j++)
				tmp[j]=x[j]+u1*GF[j];
	        fu1 = f(tmp);
        }
        else
        {
            a = u1;
            u1 = u2;
            fu1 = fu2;
            u2 = a+s2*(b-a);
			for(j=0;j<x.size();j++)
				tmp[j]=x[j]+u2*GF[j];
			fu2 = f(tmp);
        }
    }
	for(j=0;j<x.size();j++)
		tmp[j]=x[j]+u1*GF[j];
	fu1 = f(tmp);
    for(j=0;j<x.size();j++)
		tmp[j]=x[j]+u2*GF[j];
	fu2 = f(tmp);

	if (fu1<fu2)
		for(j=0;j<x.size();j++)
			tmp[j]=x[j]+u1*GF[j];
	else 
		for(j=0;j<x.size();j++)
			tmp[j]=x[j]+u2*GF[j];
	
	return tmp;		
}