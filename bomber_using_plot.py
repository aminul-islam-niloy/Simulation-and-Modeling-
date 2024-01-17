
import numpy as np
import matplotlib.pyplot as plt
def main():
                plt.title('Pure Pursuit')
                xb, yb = np.random.randint(0, 600, 2)
                xf, yf = (50, 50)
                vf = 20
                minDist = 100
                maxDist = 600
                bx=[xb]
                by=[yb]
                fx=[xf]
                fy=[yf]
                
                cnt = 0
                
                while(True):
                    cnt += 1
                    dist = np.sqrt((xb-xf)**2+(yb-yf)**2)
                    print(dist)
                   
                    if (dist <= minDist):
                        plt.text(30,47,f'Bomber caught at: {cnt}', fontsize=12)
                        plt.plot([xf, xb],[yf, yb],linestyle='-',linewidth=3)
                        print('Bomber caught at step: ' + str(cnt))
                        plt.pause(5)
                        break
                    elif (dist >= maxDist):
                        plt.plot([xf, xb],[yf, yb],linestyle='-',linewidth=3)                        
                        plt.text(30,47,f'Bomber escaped at: {cnt}', fontsize=12)
                        print('Bomber escaped at step: ' + str(cnt))
                        plt.pause(5)
                        break
                    else:
                        cosA, sinA = (xb-xf)/dist, (yb-yf)/dist
                        xf, yf = (xf+vf*cosA), (yf+vf*sinA)
                        xb, yb = np.random.randint(0, 600, 2)
                        bx.append(xb)
                        by.append(yb)
                        fx.append(xf)
                        fy.append(yf)
                        plt.scatter(xf,yf, marker='o',color='red',label='Fighter')
                        plt.plot(fx,fy,color='red')
                        plt.scatter(xb,yb, marker='o',color='green',label='Bomber')
                        plt.plot(bx,by,color='green')
                        
                        plt.pause(0.5)
                    if cnt==1:
                        plt.legend()        
                plt.show()



if __name__ == '__main__':
    main()