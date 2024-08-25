  def total(self):
      inDate = self.var_checkin.get()
      outDate = self.var_checkout.get()

      try:
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        
        if outDate < inDate:
            self.display_error_message("Checkout date cannot be earlier than check-in date")
            # Display an error message if the checkout date is earlier than the check-in date
            # You can change this part to suit your GUI framework for displaying errors
            
        else:
            self.var_noOfdays.set(abs((outDate - inDate).days))
      # except ValueError as e:
      #   try:
      #     float(inDate)
      #     float(outDate)
      #     self.display_error_message("Invalid date format.please use dd/mm/yyyy format.")
      except ValueError as e:
        if str(e) == "could not convert string to float: ''":
        # Handle a ValueError if the input dates are not in the expected format
         self.display_error_message("please")
        else:
          self.display_error_message("Invalid date format. Please use dd/mm/yyyy format.")

    def display_error_message(self, message):
    # You need to implement a method to display an error message in your specific GUI framework
    # This may involve creating a popup window, label, or message box to show the error message
    # Replace this with the appropriate code for your GUI library
      pass

      
      if (self.var_meal.get()=="BreakFast" or "breakfast" or "Breakfast" and self.var_roomtype.get()=="laxary"):
        q1=float(300)
        q2=float(700)
        q3=float(self.var_noOfdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))

        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)
        
        
      elif (self.var_meal.get()=="BreakFast" or "breakfast" or "Breakfast" and self.var_roomtype.get()=="Double"):
        q1=float(200)
        q2=float(600)
        q3=float(self.var_noOfdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))

        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)  
        
      elif (self.var_meal.get()=="BreakFast" or "breakfast" or "Breakfast" and self.var_roomtype.get()=="Single"):
        q1=float(150)
        q2=float(500)
        q3=float(self.var_noOfdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))

        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT) 
          
      
      elif (self.var_meal.get()=="Lunch" or "lunch" and self.var_roomtype.get()=="Single"):
        q1=float(300)
        q2=float(500)
        q3=float(self.var_noOfdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))

        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)  
        
        
      elif (self.var_meal.get()=="Lunch" or "lunch" and self.var_roomtype.get()=="Double"):
        q1=float(400)
        q2=float(600)
        q3=float(self.var_noOfdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))

        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT) 
        
      elif (self.var_meal.get()=="Lunch" or "lunch" and self.var_roomtype.get()=="laxary"):
        q1=float(500)
        q2=float(700)
        q3=float(self.var_noOfdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))

        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)  
        
      elif (self.var_meal.get()=="Dinner" or "dinner" and self.var_roomtype.get()=="Single"):
        q1=float(300)
        q2=float(500)
        q3=float(self.var_noOfdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))

        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT) 
        
      elif (self.var_meal.get()=="Dinner" or "dinner" and self.var_roomtype.get()=="Double"):
        q1=float(400)
        q2=float(600)
        q3=float(self.var_noOfdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))

        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)  
        
      elif (self.var_meal.get().lower() == "dinner" and self.var_roomtype.get().lower() == "luxury"):
        meal_cost = 500
        room_cost = 700
        num_of_days = float(self.var_noOfdays.get())

        total_cost = (meal_cost + room_cost) * num_of_days
        gst_rate = 0.10  # 10% GST rate
        gst_amount = total_cost * gst_rate

        total_with_gst = total_cost + gst_amount

        self.var_paidtax.set("Rs. %.2f" % gst_amount)
        self.var_actualtotal.set("Rs. %.2f" % total_cost)
        self.var_total.set("Rs. %.2f" % total_with_gst)