#include<bits/stdc++.h>
using namespace std;

vector<int> create_permutation(int height, int width){
    int i = 0, total_pixel = height*width;
    map<int, int> m;
    vector<int> per(total_pixel, 0);
    while(m.size() < total_pixel){
        int num = rand()%total_pixel;
        if(m.find(num) == m.end()){
            m[num] = 1;
            per[i++] = num;
        }
    }
    return per;
}

vector<vector<int>> create_random_color_permutation(int height, int width){
    int i, j, max_color_value = 255, total_pixel = height*width;
    vector<vector<int>> color(height, vector<int>(width, 0));
    for(i=0; i<height; i++){
        for(j=0; j<width; j++){
            int num = (rand())%max_color_value;
            color[i][j] = num;
        }
    }
    return color;
}

void create_color_S_Box_csv_file(int height, int width, vector<vector<int>> color, string file_name){
    ofstream file;
    file.open(file_name);
    int i, j;
    for(i=0; i<height; i++){
        for(j=0; j<width; j++){
            file<<color[i][j]<<",";
        }
        file<<endl;
    }
    file.close();
}

void craete_permutation_table_csv_file(vector<int> per, int height, int width, string file_name){
    ofstream file;
    file.open(file_name);
    int i, j, k = 0;
    for(i=0; i<height; i++){
        for(j=0; j<width; j++){
            file<<per[k++]<<",";
        }
        file<<endl;
    }
    file.close();
}

int main(){
    int N, height = 100, width = 300;
    int i, j;

    //-------------------- Color Shuffle Box ---------------------------------
    vector<vector<int>> red_per = create_random_color_permutation(100, 300);
    vector<vector<int>> blue_per = create_random_color_permutation(100, 300);
    vector<vector<int>> green_per = create_random_color_permutation(100, 300);
    //-------------------------------------------------------------------------

    //------------------ Create CSV File of shuffle matrix --------------------
    create_color_S_Box_csv_file(height, width, red_per, "Red_S_Box.csv");
    create_color_S_Box_csv_file(height, width, green_per, "Green_S_Box.csv");
    create_color_S_Box_csv_file(height, width, blue_per, "Blue_S_Box.csv");
    //-------------------------------------------------------------------------

    //------------------ Create Permutation Matrix ----------------------------
    vector<int> intial_permutaion = create_permutation(height, width);
    craete_permutation_table_csv_file(intial_permutaion, height, width, "Intial_Permutation.csv");
    //-------------------------------------------------------------------------
    return 0;
}
