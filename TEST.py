import segno
qrcode = segno.make('upi://pay?pa=6388574919@paytm&pn=MEC_GEAR_INDIA&am=10&tn=Thanks_for_Visit&cu=INR')
qrcode.save('yellow-submarine.pdf',scale=10, dark='darkblue')