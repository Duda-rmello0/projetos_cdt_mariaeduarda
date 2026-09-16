def atualizar_fundo_tela(self, caminho_img):
        if caminho_img and os.path.exists(caminho_img):
            try:
                pil_img = Image.open(caminho_img)
                pil_img = pil_img.resize((920, 800), Image.Resampling.LANCZOS)
                
                # Salvamos a referência para evitar que o Garbage Collector apague a imagem
                self.imagem_fundo_atual = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(920, 800))
                
                self.lbl_fundo_bg.configure(image=self.imagem_fundo_atual, text="")
                self.lbl_fundo_bg.place(x=0, y=0, relwidth=1, relheight=1)
                self.lbl_fundo_bg.lower() # Mantém estritamente no fundo
                return
            except Exception as e:
                print(f"[ERRO] Falha ao carregar fundo de tela: {e}")
        
        self.imagem_fundo_atual = None
        self.lbl_fundo_bg.configure(image="", text="")