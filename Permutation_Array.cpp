#include<bits/stdc++.h>
using namespace std;

typedef long long int lli;

vector<lli> create_permutation(lli height, lli width){
    lli i = 0, total_pixel = height*width, j = 0;
    map<lli, lli> m;
    vector<lli> per(total_pixel, 0);
    for(i=0; i<=total_pixel; i++){
        per[i] = i;
    }
    unsigned seed = 0;
    shuffle(per.begin(), per.end(), default_random_engine(seed));
//    while(m.size() < total_pixel){
//        lli num = rand()%total_pixel;
//        if(m.find(num) == m.end()){
//            m[num] = 1;
//            per[i++] = num;
//        }
//        ++j;
//        cout<<j<<endl;
//    }
    return per;
}

vector<vector<lli>> create_random_color_permutation(lli height, lli width){
    lli i, j, max_color_value = 255, total_pixel = height*width;
    vector<vector<lli>> color(height, vector<lli>(width, 0));
    for(i=0; i<height; i++){
        for(j=0; j<width; j++){
            lli num = (rand())%max_color_value;
            color[i][j] = num;
        }
    }
    return color;
}

void create_color_S_Box_csv_file(lli height, lli width, vector<vector<lli>> color, string file_name){
    ofstream file;
    file.open(file_name);
    lli i, j;
    for(i=0; i<height; i++){
        for(j=0; j<width; j++){
            file<<color[i][j]<<",";
        }
        file<<endl;
    }
    file.close();
}

void craete_permutation_table_csv_file(vector<lli> per, lli height, lli width, string file_name){
    ofstream file;
    file.open(file_name);
    lli i, j, k = 0;
    for(i=0; i<height; i++){
        for(j=0; j<width; j++){
            file<<per[k++]<<",";
        }
        file<<endl;
    }
    file.close();
}

int main(){
    lli N, height = 525, width = 525;
    lli i, j;

    //-------------------- Color Shuffle Box ---------------------------------
    vector<vector<lli>> red_per = create_random_color_permutation(height, width);
    cout<<"Red Permutation generated\n"<<endl;
    vector<vector<lli>> blue_per = create_random_color_permutation(height, width);
    cout<<"Blue Permutation generated\n"<<endl;
    vector<vector<lli>> green_per = create_random_color_permutation(height, width);
    cout<<"Green Permutation generated\n"<<endl;
    //-------------------------------------------------------------------------

    //------------------ Create CSV File of shuffle matrix --------------------
    create_color_S_Box_csv_file(height, width, red_per, "Red_S_Box.csv");
    create_color_S_Box_csv_file(height, width, green_per, "Green_S_Box.csv");
    create_color_S_Box_csv_file(height, width, blue_per, "Blue_S_Box.csv");
    //-------------------------------------------------------------------------

    //------------------ Create Permutation Matrix ----------------------------
    vector<lli> initial_permutaion = create_permutation(height, width);
    craete_permutation_table_csv_file(initial_permutaion, height, width, "Initial_Permutation.csv");
    cout<<"Initial Permutation generated\n"<<endl;
    //-------------------------------------------------------------------------
    return 0;
}
