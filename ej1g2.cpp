#include <iostream>
#include <cmath>

using namespace std;

void maxvector(int V[],int n,int & max,int & pos){
	max=V[0];
	pos=0;
	for (int i=0;i<n;i++)
		if (V[i]>max){
			max=V[i];
			pos=i;}
}
void minvector(int V[],int n,int & min,int & posmin){
	min=V[0];
	posmin=0;
	for (int i=0;i<n;i++)
		if (V[i]<min){
			min=V[i];
			posmin=i;}
}
int nroveces(int V[],int n,int k){
	int cont=0;
	for (int i=0;i<n;i++)
		if (V[i]==k)
			cont++;
	return cont;
}
int elemdif(int V[],int n){
	int cont=0;
	for (int i=0;i<n;i++){
		bool dif=true;
		for (int j=0;j<i;j++)
			if (V[j]==V[i])
				dif=false;
		if (dif==true)
			cont++;}
	return cont;
}
bool ordenado(int V[],int n){
	bool ordenado=true;
	int i=0;
	while(i<n && ordenado==true){
		for (int j=0;j<i;j++)
			if (V[j]>V[i])
				ordenado=false;
		i++;}
	return ordenado;
}
void medyvar(int V[],int n,double & media,double & varianza){
	double suma=0,suma2=0;
	for (int i=0;i<n;i++)
		suma=suma+V[i];
	media=suma/n;
	for (int i=0;i<n;i++)
		suma2=suma2+pow(V[i]-media,2);
	varianza=suma2/n;
}
void pedirvector(int V[],int n){
	for (int i=0;i<n;i++){
		cout<<"Elemento "<<i<<" del vector\n";
		cin>>V[i];
	}
}
void imprimevect(int V[],int n){
	cout<<"("<<V[0]<<",";
	for (int i=1;i<n-1;i++)
		cout<<V[i]<<",";
	cout<<V[n-1]<<")"<<endl;
}
const int TAM=5;
int main (){
	int V[TAM],min,posmin,max,posmax;
	double media,varianza;
	pedirvector(V,TAM);
	imprimevect(V,TAM);
	medyvar(V,TAM,media,varianza);
	cout<<"La media del vector es "<<media<<" y su varianza es  "<<varianza<<endl;
	cout<<ordenado(V,TAM)<<endl;
	cout<<elemdif(V,TAM)<<endl;
	cout<<nroveces(V,TAM,2)<<endl;
	minvector(V,TAM,min,posmin);
	cout<<min<<" "<<posmin<<endl;
	maxvector(V,TAM,max,posmax);
	cout<<max<<" "<<posmax;
	system("PAUSE");
	return 0;
}
