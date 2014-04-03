//
//  mainViewController.h
//  Heaped
//
//  Created by Michael Zhao on 4/2/14.
//  Copyright (c) 2014 Michael Zhao. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface mainViewController : UIViewController

@property (strong, nonatomic) IBOutlet UIButton *distanceButton;

@property (strong, nonatomic) IBOutlet UILabel *distanceField;

- (IBAction)showDistance:(id)sender;



@end
