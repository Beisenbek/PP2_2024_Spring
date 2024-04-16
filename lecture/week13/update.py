import psycopg2

def update_vendor(vendor_id, vendor_name, vendor_old_name):
    """ Update vendor name based on the vendor id """
    
    updated_row_count = 0

    sql = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_name = %s"""
    
    try:
        with psycopg2.connect(host="localhost",database="suppliers",user="postgres",password="123") as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (vendor_name, vendor_old_name))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

if __name__ == '__main__':
    update_vendor(1, "3M Corp", "3M Co.")