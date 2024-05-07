# 動かし方
## terminal 1
1. dockerの実行
    ```
    ./run.sh
    ```
1. シミュレーションの実行
    ターミナルから実行すると```Ctrl+c```でchoreonoid rosを強制終了できる．
    ```
    bash sample_env/run_sample_env.sh
    ```
## terminal 2
1. dockerの実行
    ```
    ./exec.sh run_jupyter.sh
    ```
2. jupyterの実行

    [http://localhost:8888](http://localhost:8888)にアクセスしてsample_env以下のsample_motion.ipynbを実行する．