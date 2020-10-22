#include <iostream> 
#include <cstdlib> 
#include <pthread.h> 
#include <time.h> 
  
#include<termios.h> 
#include<fcntl.h> 
  
  
#define TABLE_SIZE 20 
#define BLOCK_SIZE 4 
#define SLEEP_TIME 500 
  
using namespace std; 
  
struct grid{int x; int y;};    //坐标 
  
/////////////////////Block 类////////////////////// 
class Block 
{ 
public: 
  enum direct{UP, DOWN, LEFT, RIGHT};         //定义方向 
  grid g[BLOCK_SIZE];                 //方块的坐标信息 
  
  void def_block(grid g1, grid g2, grid g3, grid g4); //定义方块 
  void rotate();                   //旋转方块 
  void move(int dir);                 //移动方块 
  void set_cen(grid g);                //设置方块旋转中心 
  grid get_cen();                   //获取方块旋转中心 
  void set_type(int t);                //设置方块种类 
  int get_type();                   //获取方块种类 
  void back();                    //旋转还原 
  void creat_block(int x, int y);           //随机生成方块 
  
private: 
  grid center;                    //方块旋转中心 
  int type;                      //方块类型 
    
  
}; 
  
void Block::def_block(grid g1, grid g2, grid g3, grid g4) { 
  g[0]=g1; g[1]=g2; g[2]=g3; g[3]=g4; 
} 
  
void Block::rotate() { 
  int x, y, i=0; 
  
  for(i; i<=3; i++) { 
    x=g[i].x-center.x; y=g[i].y-center.y; 
    g[i].x=center.x+y; g[i].y=center.y-x; 
  } 
} 
  
void Block::move(int dir) { 
  int d=dir, i=0; 
  
  switch(d) { 
  case UP: {  
    for(i; i<=3; i++) g[i].y++; 
    center.y++; break; 
       } 
  case DOWN: { 
    for(i; i<=3; i++) g[i].y--; 
    center.y--; break; 
        } 
  case LEFT: { 
    for(i; i<=3; i++) g[i].x--; 
    center.x--; break; 
        } 
  case RIGHT: { 
    for(i; i<=3; i++) g[i].x++; 
    center.x++; break; 
        } 
  } 
} 
  
void Block::set_cen(grid g) { 
  center=g; 
} 
  
grid Block::get_cen() { 
  return center; 
} 
  
void Block::set_type(int t) { 
  type=t; 
} 
  
int Block::get_type() { 
  return type; 
} 
  
void Block::back() { 
  int x, y, i=0; 
  
  for(i; i<=3; i++) { 
    x=g[i].x-center.x; y=g[i].y-center.y; 
    g[i].x=center.x-y; g[i].y=center.y+x; 
  } 
} 
  
void Block::creat_block(int x, int y) {  //随机创建方块 
  int ran; 
  grid g[BLOCK_SIZE]; 
  
    
  ran=1+rand()%7; 
  switch(ran) { 
  //L 
  case 1: { 
    g[0].x=x/2; g[0].y=y-3; 
    g[1].x=g[0].x; g[1].y=g[0].y+1; 
    g[2].x=g[0].x; g[2].y=g[0].y+2; 
    g[3].x=g[0].x+1; g[3].y=g[0].y;  
    set_cen(g[0]); set_type(1); break; 
      } 
  //反L 
  case 2: { 
    g[0].x=x/2; g[0].y=y-3; 
    g[1].x=g[0].x; g[1].y=g[0].y+1; 
    g[2].x=g[0].x; g[2].y=g[0].y+2; 
    g[3].x=g[0].x-1; g[3].y=g[0].y;  
    set_cen(g[0]); set_type(2); break; 
      } 
  //Z 
  case 3: { 
    g[0].x=x/2; g[0].y=y-2; 
    g[1].x=g[0].x; g[1].y=g[0].y+1; 
    g[2].x=g[0].x+1; g[2].y=g[0].y+1; 
    g[3].x=g[0].x-1; g[3].y=g[0].y;  
    set_cen(g[0]); set_type(3); break; 
      } 
  //反Z 
  case 4: { 
    g[0].x=x/2; g[0].y=y-2; 
    g[1].x=g[0].x; g[1].y=g[0].y+1; 
    g[2].x=g[0].x+1; g[2].y=g[0].y+1; 
    g[3].x=g[0].x-1; g[3].y=g[0].y;  
    set_cen(g[0]); set_type(4); break; 
      } 
  //田 
  case 5: { 
    g[0].x=x/2; g[0].y=y-2; 
    g[1].x=g[0].x; g[1].y=g[0].y+1; 
    g[2].x=g[0].x+1; g[2].y=g[0].y+1; 
    g[3].x=g[0].x+1; g[3].y=g[0].y;  
    set_cen(g[0]); set_type(5); break; 
      } 
  //1 
  case 6: { 
    g[0].x=x/2; g[0].y=y-3; 
    g[1].x=g[0].x; g[1].y=g[0].y+1; 
    g[2].x=g[0].x; g[2].y=g[0].y+2; 
    g[3].x=g[0].x; g[3].y=g[0].y-1;  
    set_cen(g[0]); set_type(6); break; 
      } 
  //山 
  case 7: { 
    g[0].x=x/2; g[0].y=y-2; 
    g[1].x=g[0].x; g[1].y=g[0].y+1; 
    g[2].x=g[0].x-1; g[2].y=g[0].y; 
    g[3].x=g[0].x+1; g[3].y=g[0].y;  
    set_cen(g[0]); set_type(7); break; 
      } 
  default: ; 
  } 
  def_block(g[0], g[1], g[2], g[3]); 
} 
  
  
///////////////////////////////////////// 
  
////////////////////Table 类////////////////////// 
class Table 
{ 
public: 
    
  Table() {             //构造棋盘 
    height=20; width=10; count=0; 
    init_table(); 
  } 
  Table(int x, int y); 
  int set_block(Block bl);     //安设方块 
  void clr_block(Block bl);     //清除方块 
  int clr_line(int y);       //消行 
  int get_h();           //获取棋盘高度 
  int get_w();           //获取棋盘宽度 
  int if_full(int y);        //判定是否满行 
  int get_table(int x, int y);   //获取棋盘上点信息 
  void paint();           //绘制棋盘 
  void move_line(int y);      //整行下移 
  void set_count(int c);      //记录得分 
  int get_count();         //获取得分 
  
private: 
  int table[TABLE_SIZE][TABLE_SIZE];//棋盘 
  int height, width;        //棋盘的高和宽 
  int count;            //得分 
  
  void init_table();        //棋盘初始化 
  
}; 
  
void Table::init_table() { 
  int i=0, j=0; 
  
  for(i; i<width; i++) { 
    for(j=0; j<height; j++) { 
      table[i][j]=0; 
    } 
  } 
} 
  
Table::Table(int x, int y) { 
  height=y; width=x; count=0; 
  init_table(); 
} 
  
int Table::set_block(Block bl) { 
  int x, y; 
  int i; 
  for(i=0; i<=3; i++) { 
    x=bl.g[i].x; y=bl.g[i].y; 
    if(table[x][y]!=0 || x>=width || x<0 || y>=height || y<0) { 
      return 0; 
    } 
  } 
  for(i=0; i<=3; i++) { 
    x=bl.g[i].x; y=bl.g[i].y; 
    table[x][y]=1; 
  } 
  return 1; 
} 
  
void Table::clr_block(Block bl) { 
  int x, y; 
  
  for(int i=0; i<=3; i++) { 
    x=bl.g[i].x; y=bl.g[i].y; 
    table[x][y]=0; 
  } 
} 
  
int Table::clr_line(int y) { 
  if(y<0 || y>=height) return 0; 
  for(int i=0; i<width; i++) { 
    table[i][y]=0; 
  } 
  return 1; 
} 
  
int Table::get_h() { 
  return height; 
} 
  
int Table::get_w() { 
  return width; 
} 
  
int Table::if_full(int y) { 
  int i=0; 
  
  for(i; i<width; i++) { 
    if(table[i][y]==0) return 0; 
  } 
  return 1; 
} 
  
int Table::get_table(int x, int y) { 
  return table[x][y]; 
} 
  
void Table::paint() { 
  int i, j; 
  
  for(i=0; i<width+2; i++) cout<<"-"<<flush; 
  cout<<"\n"<<flush; 
  for(i=height-1; i>=0; i--) { 
    cout<<"|"<<flush; 
    for(j=0; j<width; j++) { 
      if(table[j][i]==0) cout<<" "<<flush; 
      else cout<<"▣"<<flush; 
    } 
    if(i==10) 
      cout<<"|  得分："<<get_count()<<endl; 
    else if(i==7) 
      cout<<"|  Press 'q' to quit!"<<endl; 
    else
      cout<<"|"<<endl; 
  } 
  for(i=0; i<width+2; i++) cout<<"-"<<flush; 
  cout<<"\n"<<flush; 
  //cout<<"得分："<<get_count()<<endl; 
} 
  
void Table::move_line(int y) { 
  int i, j; 
  
  for(i=y; i<height-1; i++) { 
    for(j=0; j<width; j++) { 
      table[j][i]=table[j][i+1]; 
    } 
  } 
} 
  
void Table::set_count(int c) { 
  count+=c; 
} 
  
int Table::get_count() { 
  return count; 
} 
  
/////////////////////////////////////////////////////// 
class Mythread 
{ 
public: 
  void init(); 
  static void *getkey(void *arg);//线程函数在类里面定义必须定义为static型，以去除类指针。 
  static void *paint_loop(void *arg); 
}; 
  
void Mythread::init() 
{ 
  pthread_t ntid,ntid2; 
  int err,err2;     
  err = pthread_create(&ntid,NULL,getkey,NULL); 
  err2 = pthread_create(&ntid2,NULL,paint_loop,NULL); 
  if(err != 0 || err2 != 0){ 
    cout<<"can't create thread!"<<endl; 
    exit(0); 
  } 
} 
  
unsigned char flag=1,buf[2];//全局变量 
Table tab(15, 20); //构造一个15,20的棋盘 
Block bl;      //构造一个落下方块 
void* Mythread::paint_loop(void *arg) 
{ 
  while(1) 
  { 
    system("clear"); 
    tab.paint(); 
    usleep(50000);    //暂停50 MS 
  } 
} 
void* Mythread::getkey(void *arg) 
{ 
  struct termios saveterm,nt; 
  fd_set rfds,rs; 
  struct timeval tv; 
  int i=0,q,r,fd=0; 
  tcgetattr(fd,&saveterm); 
  nt=saveterm; 
  
  nt.c_lflag &= ~ECHO; 
  nt.c_lflag &= ~ISIG; 
  nt.c_lflag &= ~ICANON; 
  
  tcsetattr(fd,TCSANOW,&nt); 
  
  FD_ZERO(&rs); 
  FD_SET(fd,&rs); 
  tv.tv_sec=0; 
  tv.tv_usec=0; 
  while(1) 
  {   
    read(0,buf,1); 
    r=select(fd+1,&rfds,NULL,NULL,&tv); 
    if(r<0) 
    { 
      write(1,"select() error.\n",16); 
    } 
    rfds=rs; 
    if(flag==2||buf[0]==113)//游戏结束或者用户按下'q'键，则程序退出 
    { 
      tcsetattr(0,TCSANOW,&saveterm); 
      exit(0); 
    } 
    if(buf[0]<=68&&buf[0]>=65) flag=0;//如果按的键是方向键，则将标志位置0并执行相应的处理. 
    if(flag==0) 
    { 
      if(buf[0]==65) { 
      //if(dir!=0) { 
        if(bl.get_type()==5) continue; //如果出现田字形则不作旋转 
        tab.clr_block(bl);      //清空方块上一次位置 
        bl.rotate();         //开始旋转 
        if(!tab.set_block(bl)) {   //将旋转后的方块写在棋盘上 
          bl.back();       //如果写失败(例如到边线了，或卡住了)则还原旋转前位置 
          continue; 
          tab.set_block(bl);     
        } 
      } 
      //下（加速下落） 
      //dir=GetAsyncKeyState(VK_DOWN);  //获取向下 
      if(buf[0]==66) { 
        tab.clr_block(bl);     //清空方块上一次位置 
        bl.move(bl.DOWN);      //向下移动一步 
        if(!tab.set_block(bl)) {  //将移动后的方块写在棋盘上 
          bl.move(bl.UP);     //如果失败，则还原到移动前的位置（即上移一步） 
          tab.set_block(bl); 
        } 
      } 
      //左（左移） 
      //dir=GetAsyncKeyState(VK_LEFT); 
      if(buf[0]==68) { 
        tab.clr_block(bl); 
        bl.move(bl.LEFT); 
        if(!tab.set_block(bl)) { 
          bl.move(bl.RIGHT); 
          tab.set_block(bl); 
        } 
      } 
      //右（右移） 
      //dir=GetAsyncKeyState(VK_RIGHT); 
      if(buf[0]==67) { 
        tab.clr_block(bl); 
        bl.move(bl.RIGHT); 
        if(!tab.set_block(bl)) { 
          bl.move(bl.LEFT); 
          tab.set_block(bl); 
        } 
      } 
      flag=1; 
    } 
  } 
  tcsetattr(0,TCSANOW,&saveterm); 
} 
  
////////////主函数部分/////////////////////// 
  
int main() 
{ 
  //Table tab(15, 20); //构造一个15,20的棋盘 
  //Block bl;      //构造一个落下方块 
  Mythread thread; 
  thread.init(); 
  int dir,i,c; 
  while(true) { 
    //生成方块 
    srand(time(0)); 
    bl.creat_block(tab.get_w(), tab.get_h()); 
    //判断游戏是否结束 
    if( !tab.set_block(bl) ) { 
      system("clear"); 
      cout<<"GAME OVER!"<<endl; 
      flag=2; 
      cout<<"PRESS ANY KEY TO CONTINUE!"<<endl; 
      while(1); 
    } 
    ///////////行动按键判定 
    while(true){ 
      usleep(500000);    //暂停500 MS 
      /////////////向下移动一格 
      tab.clr_block(bl);    //清空上一次方块位置 
      bl.move(bl.DOWN);    //向下移动一步 
      if(!tab.set_block(bl)) {   //是否触底 
        bl.move(bl.UP);    //如果触底，还原触底前位置 
        tab.set_block(bl); 
        break; 
      } 
    } 
    //如果满行则消行 
    for(i=0; i<tab.get_h(); i++) { 
      if(tab.if_full(i)) { //是否满行 
        tab.clr_line(i); //如果是，消行 
        tab.move_line(i); //将所消行的上面的棋盘信息下移 
        i--;      //下移后，重新检查这一行是否满（可能出现几行同时消去） 
        tab.set_count(100); //记录得分 
      } 
    } 
      
  } 
  return 0; 
}