from flask import Flask, render_template

app=Flask(__name__)

@app.route('/') 
def home():
    return render_template('home.html')

class App: 
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        if(usu == "root" and password == "1234"):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="lacontrasseña no es correcta",title="mensaje")

@app.route('/about')
def about():
    return render_template('About.html')

if __name__ == '__main__':
    app.run(debug=True)