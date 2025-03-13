class Matrix {

    Integer[][] mat;

    int n , m;

    private static Integer[] zero_arr (int size) {
        Integer[] ret = new Integer[size];
        for (int i = 0; i < size; i++) ret[i] = 0;
        return ret;
    }

    public static Matrix brute_mult (Matrix a, Matrix b) {

        assert(a.m == b.n);
        Matrix rez = new Matrix(a.n,b.m, zero_arr(a.n*b.m));

        for (int i = 0; i < a.n; i++) {
            for (int j = 0; j < b.m; j++) {
                
                for (int k = 0; k < a.m; k++) {
                    rez.mat[i][j] += a.mat[i][k] * b.mat[k][j];
                }
            }
        }

        return rez;

    }

    public static Matrix neg (Matrix a) {

        for (int i = 0; i < a.n; i++) {
            for (int j = 0; j < a.m; j++) {
                a.mat[i][j] = -a.mat[i][j];
            }
        }
        return a;
    }

    Matrix (int _n , int _m , Integer[] entries) {
        n = _n; m = _m;
        mat = new Integer[n][m];
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                mat[i][j] = entries[cnt++];
            }
        } 

    }


    public static Matrix I (int n) {
        
        Integer[] arr = new Integer[n*n];
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) arr[cnt++] = 1;
                else arr[cnt++] = 0;
            }
        }
        Matrix i = new Matrix(n,n,arr);

        return i;
    }

    public void print () {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(mat[i][j]);
                System.out.print(" ");
            }
            System.out.print('\n');
        }
    }

    public static Matrix strassen_mult (Matrix a , Matrix b) {
        assert(a.m == b.n);

        if (a.m == 1) {
            Integer[] arr = {a.mat[0][0] * b.mat[0][0]};
            return new Matrix(1 , 1 , arr);
        }
        
        Matrix[][] A = block_division_strassen(a);
        Matrix[][] B = block_division_strassen(b);

        Matrix M1 = strassen_mult(add(A[0][0] , A[1][1]), add(B[0][0] , B[1][1]));
        Matrix M2 = strassen_mult(add(A[1][0] , A[1][1]), B[0][0]);
        Matrix M3 = strassen_mult(A[0][0], add(B[0][1] , neg(B[1][1])));
        Matrix M4 = strassen_mult(A[1][1], add(B[1][0] , neg(B[0][0])));
        Matrix M5 = strassen_mult(add(A[0][0] , A[0][1]), B[1][1]);
        Matrix M6 = strassen_mult(add(A[1][0] , neg(A[0][0])), add(B[0][0],B[1][2]));
        Matrix M7 = strassen_mult(add(A[0][1] , neg(A[1][1])), add(B[1][0] , B[1][1]));
        
        Matrix[][] C = new Matrix[2][2];

        Matrix[] C00 = {M1 , M4 , neg(M5) , M7};
        Matrix[] C01 = {M3 , M5};
        Matrix[] C10 = {M2 , M4};
        Matrix[] C11 = {M1 , neg(M2) , M3 , M6};

        C[0][0] = add(C00);
        C[0][1] = add(C01);
        C[1][0] = add(C10);
        C[1][1] = add(C11);
        
        Matrix rez = unite_blocks(C);
        return rez;
    }

    
    public static Matrix unite_blocks (Matrix[][] blocs) {
        boolean valid = true;

        int size_n = 0 , size_m = 0;
        for (int i = 0; i < blocs.length; i++) {
            size_n += blocs[i][0].n;
        }

        for (int j = 1; j < blocs[0].length; j++) {
            int sz_n_here = 0;
            for (int i = 0; i < blocs.length; i++) {
                sz_n_here += blocs[i][j].n;
            }
            valid |= (sz_n_here == size_n);

        }

        for (int j = 0; j < blocs[0].length; j++) {
            size_m += blocs[0][j].m;
        }

        for (int i = 1; i < blocs.length; i++) {
            int sz_m_here = 0;
            for (int j = 0; j < blocs[i].length; j++) {
                sz_m_here += blocs[i][j].m;
            }
            valid |= (sz_m_here == size_m);
        }
        assert (valid);

        Integer[] build = new Integer[size_n * size_m];

        int cnt = 0;

        for (int bi = 0; bi < blocs.length; bi++) {
            for (int i = 0; i < blocs[bi][0].n; i++){
                for (int bj = 0; bj < blocs[bi].length; bj++) {
                    for (int j = 0; j < blocs[bi][0].m; j++) {
                        build[cnt++] = blocs[bi][bj].mat[i][j];
                    }
                }
            }
        }

        Matrix ret = new Matrix(size_n , size_m , build);

        return ret;

    }

    private static Matrix[][] block_division_strassen (Matrix a) {

        Matrix[][] ret = new Matrix[2][2];

        int half_n = a.n / 2;
        int compl = a.n - half_n;

        ret[0][0] = new Matrix(half_n , half_n , zero_arr(half_n*half_n));
        ret[0][1] = new Matrix(half_n, compl - half_n, zero_arr(half_n*(compl)));
        ret[1][0] = new Matrix(compl , half_n , zero_arr(half_n*(compl)));
        ret[1][1] = new Matrix(compl, compl, zero_arr((compl)*(compl)));


        for (int i = 0; i < half_n; i++) {
            for (int j = 0; j < half_n; j++) {
                ret[0][0].mat[i][j] = a.mat[i][j];
            }
        }

        for (int i = 0; i < half_n; i++) {
            for (int j = half_n; j < a.m; j++) {
                try
                { ret[0][1].mat[i][j-half_n] = a.mat[i][j]; }
                catch(Exception PULA) { System.out.printf("%d %d %d %d\n" , i , j , a.n , a.m); }
            }
        }


        for (int i = half_n; i < a.n; i++) {
            for (int j = 0; j < half_n; j++) {
                ret[1][0].mat[i-half_n][j] = a.mat[i][j];
            }
        }
        
        for (int i = half_n; i < a.n; i++) {
            for (int j = half_n; j < a.n; j++) {
                ret[1][1].mat[i-half_n][j-half_n] = a.mat[i][j];
            }
        }

        return ret;
    }

    public static Matrix add (Matrix a , Matrix b) {
        assert (a.n == b.n && a.m == b.m);
        Integer[] arr = new Integer[a.n * a.m];
        int cnt = 0;
        for (int i = 0; i < a.n; i++) {
            for (int j = 0; j < a.m; j++) {
                arr[cnt++] = a.mat[i][j] + b.mat[i][j];
            }
        }
        Matrix ret = new Matrix(a.n , a.m , arr);
        return ret;
    }

    public static Matrix add (Matrix[] mat_list) {
        Matrix ret = new Matrix(mat_list[0].n , mat_list[0].m , zero_arr(mat_list[0].n * mat_list[0].m));

        for (int i = 0; i < mat_list.length; i++) {
            ret = add(ret , mat_list[i]);
        }

        return ret;

    }


    public static void main (String[] args) {
        Integer[] arrm1 = {1,0,0,0,
                           0,1,0,0,
                           0,0,1,0,
                           0,0,0,1};
        Integer[] arrm2 =  {1,0,5,0,
                            0,1,0,0,
                            0,9,1,3,
                            0,7,0,1};
        Matrix m1 = new Matrix(4 , 4 , arrm1);
        Matrix m2 = new Matrix(4 , 4 , arrm2);

        strassen_mult(m1, m2).print();
    }

}
